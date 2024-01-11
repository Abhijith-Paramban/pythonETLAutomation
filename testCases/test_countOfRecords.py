import pandas as pd
import pytest
from utilities.customLogger import LogGen

class TestSQLQueries:
    # @pytest.Mark.regression
    def test_validatecount(self,db_engine):
        source_query = "SELECT COUNT(*) As record_count FROM ACA_CRR_STG..STG_DDA_1212"
        target_query = "SELECT COUNT(*) As record_count FROM ACA_CRR_STG..STD_DDA_1212"
        self.df = pd.read_sql(source_query, db_engine)
        source_count = self.df['record_count'].iloc[0]
        self.df = pd.read_sql(target_query, db_engine)
        target_count = self.df['record_count'].iloc[0]
        print('\n',source_count)
        print(target_count)
        if source_count == target_count:
            print("Test Passed")
            assert True
            db_engine.dispose()
        else:
            assert False
            db_engine.dispose()



