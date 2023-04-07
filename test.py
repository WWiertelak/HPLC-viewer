from HPLC_Viewer import HPLC_Viewer
import pandas as pd

viewer = HPLC_Viewer("TEST")


path_name = ''
db = pd.read_excel(path_name+'data_test.xlsx')
gu = pd.read_excel(path_name+'Dextran_standard.xlsx')

viewer.load_data(db, 40)
viewer.clean_data(10,30)
viewer.load_GU(gu)
viewer.scale()
viewer.plot()

