class StateMachine:

    def __init__(self):
        self.states = {}
        self.startState = None
        self.endStates=[]

    def addState(self, item):
        self.states[item.getName()] = item.run

    def setStartState(self, item):
        self.startState = item.getName()

    def run(self, info):
        try:
            handler = self.states[self.startState]
        except:
            print("Start State Not defined")
        while True:
            (newState, info) = handler(info)
            if newState in self.endStates:
                print("End")
            else:
                handler = self.states[newState]





