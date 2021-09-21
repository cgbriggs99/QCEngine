from typing import Any, Dict, Union

from .model import ProcedureHarness

class DTRProcedure(ProcedureHarness) :
    _defaults = {"name": "dtr", "procedure": "energy"}

    class Config(ProcedureHarness.Config):
        pass
    def build_input_model(self, data: Unnion[Dict[str, Any], "DTRInput"]) -> "DTRInput" :
        return self._build_model(data, DTRInput)

    def compute(self, input_model: "DTRInput", config: "TaskConfig") -> "DTRResult":
        input_data = input_model.dict()

        
