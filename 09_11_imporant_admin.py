from privileges_import import User # type: ignore
from privileges_import import Admin # type: ignore
from privileges_import import Privileges # type: ignore

admin= Admin('Michael', 'Ferrey', '18', 'male', 'Alrbight College')
admin.greet_user()
admin.describe_user()
admin.privileges.show_privileges()
