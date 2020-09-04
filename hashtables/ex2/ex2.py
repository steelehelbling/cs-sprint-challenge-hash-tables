#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    inside = {}
    route = [None] * length

    for item in tickets:
        inside[item.source] = item.destination
    itemshift = inside["NONE"]

    for grab in range(0, length):
        route[grab] = itemshift
        itemshift = inside[itemshift]
    return route

if __name__ == "__main__":
    ticket_1 = Ticket("NONE", "PDX")
    ticket_2 = Ticket("PDX", "DCA")
    ticket_3 = Ticket("DCA", "NONE")

    tickets = [ticket_1, ticket_2, ticket_3]

    expected = ["PDX", "DCA", "NONE"]
    result = reconstruct_trip(tickets, 3)
    print(result)