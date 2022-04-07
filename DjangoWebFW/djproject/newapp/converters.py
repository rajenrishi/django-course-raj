from datetime import date

class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        # check DB if question number is available
        return int(value)

    def to_url(self, value):
        return '%04d' % value


# class DateConverter:
#     regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
#
#     def to_python(self, value):
#         # check DB if question number is available
#         dt_parts = value.split('-')
#         print("dt_parts>>>>", dt_parts)
#         value = date(int(dt_parts[0]), int(dt_parts[1]), int(dt_parts[2]))
#         print("dt_obj", value)
#         return value
#
#     def to_url(self, value):
#         print("value.join", value.join('-'))
#         return value.join('-')

class DateConverter:
    regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value):
        # check DB if question number is available
        dt_parts = value.split('-')
        print("dt_parts>>>>", dt_parts)
        print("to python: ", value)
        print("to python: ", type(value))
        # check DB if question number is available
        dt_parts = value.split('-')
        print("dt_parts>>>>", dt_parts)
        value = date(int(dt_parts[0]), int(dt_parts[1]), int(dt_parts[2]))
        print("dt_obj", value)
        return value

    def to_url(self, value):
        print("to to_url: ", value)
        print("to to_url: ", type(value))
        return value
