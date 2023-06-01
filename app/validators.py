from django.forms import ValidationError

class MaxFileSiceValidator:
    def __init__(self, max_file_size=5):
        self.max_file_size =max_file_size

    def __call__(self, value):
        file_size = value.size

        max_size = self.max_file_size * 1048576

        if file_size > max_size:
            raise ValidationError(f"El peso maximo del archivo no debe ser mayor a {self.max_file_size}MB")
        return value