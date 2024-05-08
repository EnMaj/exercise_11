import random
import pygame


class Molecule:

    def __init__(self):
        self.__radius = 20
        self.__size = random.randint(5, 20)
        self.__R = random.randint(40, 255)
        self.__G = random.randint(40, 255)
        self.__B = random.randint(40, 255)
        self.__coordinate_x = random.randint(0, 900)
        self.__coordinate_y = random.randint(0, 600)
        self.__color = [self.__R, self.__G, self.__B]
        self.__speed_x = random.randint(-10, 10)
        self.__speed_y = random.randint(-10, 10)

    @property
    def size(self):
        return self.__size

    @property
    def coordinate_x(self):
        return self.__coordinate_x

    @property
    def coordinate_y(self):
        return self.__coordinate_y

    @property
    def color(self):
        return self.__color

    @property
    def radius(self):
        return self.__radius

    def check_hit(self, set_molecules):
        for molecule in set_molecules:
            if ((molecule.coordinate_x - molecule.radius) < self.__coordinate_x <
                    molecule.coordinate_x + molecule.radius):
                if (molecule.coordinate_y - molecule.radius < self.__coordinate_y <
                        molecule.coordinate_y + molecule.radius):
                    return False
        return True

    def drow_molecule(self, screenX, screenY, set_molecules):
        self.__coordinate_x += self.__speed_x
        self.__coordinate_y += self.__speed_y
        pygame.draw.circle(screen, self.__color, [self.__coordinate_x, self.__coordinate_y],
                           self.__radius, 0)
        if ((self.__coordinate_x + self.__radius >= screenX) or
            (self.__coordinate_x <= self.__radius)) or self.check_hit(set_molecules) == False:  # Условия отражения
            self.__speed_x = -self.__speed_x
        if ((self.__coordinate_y + self.__radius >= screenY) or
            (self.__coordinate_y <= self.__radius)) or self.check_hit(set_molecules) == False:
            self.__speed_y = -self.__speed_y


pygame.init()
screenX = 900
screenY = 600
screen = pygame.display.set_mode([screenX, screenY])
screen.fill([0, 0, 0])  # black

number_molecules = int(input('Введите количество молекул: '))
array_molecules = []
for _ in range(number_molecules):
    new_molecule = Molecule()
    array_molecules.append(new_molecule)

running = True
while running:
    screen.fill([0, 0, 0])
    for i in range(len(array_molecules)):
        new_set_molecules = array_molecules.copy()
        new_set_molecules.pop(i)
        array_molecules[i].drow_molecule(screenX, screenY, new_set_molecules)
    pygame.time.delay(20)  # задержка на 20 милисекунд
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
