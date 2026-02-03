import pandas as pd
import io

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import EquipmentUpload


@method_decorator(csrf_exempt, name='dispatch')
class UploadCSV(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        file = request.FILES.get('file')

        if not file:
            return Response(
                {"error": "No file uploaded"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # ✅ FIX: convert bytes → text before pandas reads it
            df = pd.read_csv(
                io.TextIOWrapper(file.file, encoding='utf-8'),
                sep=None,
                engine='python'
            )

            # Clean column names
            df.columns = [col.strip() for col in df.columns]

            required_columns = [
                'Flowrate',
                'Pressure',
                'Temperature',
                'Type',
                'Equipment Name'
            ]

            for col in required_columns:
                if col not in df.columns:
                    return Response(
                        {"error": f"Missing column: {col}"},
                        status=status.HTTP_400_BAD_REQUEST
                    )

            summary_list = []

            for _, row in df.iterrows():
                equipment = EquipmentUpload.objects.create(
                    name=str(row['Equipment Name']),
                    summary={
                        "Flowrate": float(row['Flowrate']),
                        "Pressure": float(row['Pressure']),
                        "Temperature": float(row['Temperature']),
                        "Type": str(row['Type'])
                    }
                )
                summary_list.append(equipment.summary)

            return Response(
                {
                    "total_equipment": len(summary_list),
                    "summary": summary_list
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )