"""パラメータ"""





"""コンテキスト"""
class Program:
    def __init__(self,setting,work,cutting_condition,process):
        self.setting = setting
        self.work = work
        self.cutting_condition = cutting_condition
        self.process = process

    def tool_select(self):
        self.process.tool_select(self)

    def positioning(self):
        self.process.positioning(self)

    def cutting(self):
        self.process.cutting(self)

    def returning(self):
        self.process.returning(self)

    def output_program(self):
        self.process.output_program(self)



"""設定"""

#抽象
class Setting:
    def __init__(self,head,sp,margin):
        pass


""" ワーク """
#抽象
class Work:
    def __init__(self,length,diameter):
        pass


"""切削条件"""
#抽象
class CuttingCondition:
    def __init__(self,work,velocity,feed,ap):
        pass



"""加工工程"""
# プログラムの出力を抽象化したクラス(抽象戦略)
class Process:
    def __init__(self):
        pass

    def tool_select(self):
        pass

    def positioning(self):
        pass

    def cutting(self):
        pass

    def returning(self):
        pass
    
    def output_program(self):
        raise 'Called abstract method !!'
