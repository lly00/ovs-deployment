import random


class Flow(object):
    def __init__(self, label=0, swtiches=[], key=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = label
        self.swtiches = swtiches
        self.key = key

    def randomSwitchs(self, flowLength, switchN):
        # while len(self.swtiches) < flowLength:
        #     ran = random.randint(1, switchN)
        #     if ran not in self.swtiches:
        #         self.swtiches.append(ran)
        # print(switchN,flowLength)
        self.swtiches = random.sample(range(1, switchN + 1), flowLength)


class Switch(object):
    def __init__(self, label=0, flows=[], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = label
        self.flows = flows

    def passedFlows(self, allFlows):
        for flow in allFlows:
            if self.label in flow.swtiches:
                self.flows.append(flow.label)


def init(flowN, switchN, keyRate):
    flows = []
    for i in range(flowN):
        flow = Flow(key=random.random() < keyRate)
        flow.randomSwitchs(random.randint(1, switchN), switchN)
        flow.label = i + 1
        flows.append(flow)
    return flows


flows = init(5, 10, 0.5)
for flow in flows:
    print(flow.swtiches)
    print(flow.key)
