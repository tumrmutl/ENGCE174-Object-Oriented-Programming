import pandas as pd
df = pd.read_csv( 'student.csv' )
df_selected = df[ ['First Name', 'Age'] ].sort_values( 'Age' )

# import pandas as pd
# df = pd.read_csv('students.csv')
# df_selected = df[['First Name', 'Age']].sort_values('Age')
# print(df_selected)