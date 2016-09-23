class RegionResponse:
    """docstring for RegionResponse"""

    def __init__(self, success=True, message='', rows=''):
        self.success = success
        self.message = message
        self.rows = rows
