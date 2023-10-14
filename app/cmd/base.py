from typing import Any

from app.export.excel.export_results import update_data


class BaseCmd:
    def __init__(self):
        params = self._get_the_missing_parameters(self._get_vars())
        params['method'] = self.method
        params['type_of_calculations'] = self.type_of_calculations
        self.__dict__ = params

    @staticmethod
    def _get_the_missing_parameters(params: dict[str, Any]) -> dict[str, Any]:
        for parameter, value in params.items():
            if value is None:
                print(f'Please enter: {parameter}', end=' ')
                params[parameter] = float(input())

        return params

    def _finish(self):
        print("Ответ: ", *self.answer)
        update_data(self.type_of_calculations, self.method, **self._get_vars())

    def _get_vars(self):
        params = {key: value for key, value in vars(self).items() if not key.startswith('_')}
        params.pop('type_of_calculations')
        params.pop('method')
        return params
