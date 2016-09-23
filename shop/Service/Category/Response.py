class CategoryResponse:
    """docstring for Category"""
    def __init__(self, success=True, message='', rows=''):
        self.success = success
        self.message = message
        self.rows = rows