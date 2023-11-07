class Truck:
    def __init__(self, weight, location):
        self.weight = weight
        self.location = location
    
    def setLocation(self):
        self.location += 1
    
    def getLocation(self):
        return self.location
    def getWeight(self):
        return self.weight
    
def solution(bridge_length, weight, truck_weights):
    answer = 0
    current_weight_in_bridge = 0
    current_trucks_in_bridge = []
    trucks = [Truck(truck_weights[i], 0) for i in range(len(truck_weights))]
    
    while len(current_trucks_in_bridge) > 0 or len(trucks) > 0:
        if len(trucks) > 0 and current_weight_in_bridge + trucks[0].getWeight() <= weight:
            temp_truck = trucks.pop(0)
            current_weight_in_bridge += temp_truck.getWeight()
            current_trucks_in_bridge.append(temp_truck)

        for truck in current_trucks_in_bridge:
            truck.setLocation()

        for truck in current_trucks_in_bridge:
            if truck.getLocation() == bridge_length:
                finished_truck = current_trucks_in_bridge.pop(0)
                current_weight_in_bridge -= finished_truck.getWeight()

        answer += 1

    return answer + 1