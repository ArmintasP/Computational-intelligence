import matplotlib.pyplot as plt

class Graph():
    def __init__(self) -> None:   
        self.figure, self.axis = plt.subplots(2,2, figsize=(14,6))
        plt.subplots_adjust(
           left=0.1,
           bottom=0.1,
           right=0.9,
           top=0.9,
           wspace=0.2,
           hspace=0.6)
        for ax in self.axis.flat:
            ax.set(xlabel= 'Epochų skaičius', ylabel= 'Reiškmė')
            
        
        self.training_accuracies = []
        self.training_losses = []
        self.validation_accuracies = []
        self.validation_losses = []
        self.epochs = []
    
    
    def draw_graphs(self, epoch, accuracy, loss, train):
        if train:
            self.epochs.append(epoch)
            self.training_accuracies.append(accuracy)
            self.training_losses.append(loss)
            
            self.axis[0, 0].plot(self.epochs, self.training_accuracies, 'tab:cyan')
            self.axis[0, 0].set_title('Treniravimo tikslumas')
            self.axis[0, 1].plot(self.epochs, self.training_losses, 'tab:pink')
            self.axis[0, 1].set_title('Treniravimo nuostolių funkcija')
        else:
            self.validation_accuracies.append(accuracy)
            self.validation_losses.append(loss)
            
            # self.axis[1, 1].plot(self.epochs, self.validation_losses, 'tab:olive')
            # self.axis[1, 1].set_title('Validavimo nuostolių funkcija')
            self.axis[1, 0].plot(self.epochs, self.validation_accuracies, 'tab:purple')
            self.axis[1, 0].set_title('Validavimo tikslumas')
