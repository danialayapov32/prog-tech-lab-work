from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
import json
import pandas as pd

class KpiEndpoint:
    
    def __init__(self, plotter_service):
        self.app = FastAPI()
        self.plotter = plotter_service  
        self.app.post("/kpi")(self.handle_kpi_request)

    async def handle_kpi_request(self, preset: str = Form(...), file: UploadFile = File(...)):
        preset_dict = json.loads(preset)
        df = pd.read_csv(file.file)

        path = self.plotter.make_plot(df, preset_dict)

        return FileResponse(path, media_type="image/png")
