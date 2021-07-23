class MoessnerSequence:
    sequence = []
    container = []
    indicies = []
    result = []

    def __init__(self, size, genretor):
        self.sequence = [genretor(i) for i in range(1, size+1)]
        self.indicies = list(map(lambda x: x-1, self.sequence))
        self.container = list(range(1, self.sequence[-1]+1))

        self.moessnerSum()
        self.result.sort()

    def moessnerSum(self):
        while len(self.indicies) != 0:
            #REMOVAL...
            for i in range(len(self.indicies)-1,-1,-1):
                remove_index = self.indicies[i]

                if remove_index == 0:
                    self.result.append( self.container[remove_index] )
                    del self.indicies[i]

                elif remove_index == len(self.container)-1:
                    if self.container[remove_index-1] == 0:
                        self.result.append( self.container[remove_index] )
                        del self.indicies[i]

                elif self.container[remove_index+1] == 0 and self.container[remove_index-1] == 0:
                    self.result.append( self.container[remove_index] )
                    del self.indicies[i]

                elif self.indicies[i-1] == self.indicies[i]-1:
                    self.result.append( self.container[remove_index] )
                    del self.indicies[i]

                self.container[remove_index] = 0

            self.indicies = list(map(lambda x: x-1, self.indicies))

            #ADDITION...
            last_num = 0
            for i in range(len(self.container)):
                if self.container[i] == 0:
                    continue
                self.container[i] = self.container[i] + last_num
                last_num = self.container[i]

    def __str__(self):
        return str(self.result)