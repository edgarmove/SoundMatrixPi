import pygame.mixer

pygame.mixer.init(48000, -16, 1, 1024)

soundOne = pygame.mixer.Sound("/home/pi/python_games/match0.wav")
soundTwo = pygame.mixer.Sound("/home/pi/python_games/match1.wav")
soundThree = pygame.mixer.Sound("/home/pi/python_games/match2.wav")
soundFour = pygame.mixer.Sound("/home/pi/python_games/match3.wav")
soundFive = pygame.mixer.Sound("/home/pi/python_games/match5.wav")
soundSix = pygame.mixer.Sound("/home/pi/python_games/badswap.wav")
soundSeven = pygame.mixer.Sound("/home/pi/python_games/match0.wav")
soundEight = pygame.mixer.Sound("/home/pi/python_games/match1.wav")
soundNine = pygame.mixer.Sound("/home/pi/python_games/match2.wav")
soundTen = pygame.mixer.Sound("/home/pi/python_games/match3.wav")
soundEleven = pygame.mixer.Sound("/home/pi/python_games/match4.wav")
soundTwelve = pygame.mixer.Sound("/home/pi/python_games/match5.wav")
soundThirteen = pygame.mixer.Sound("/home/pi/python_games/match0.wav")
soundFourteen = pygame.mixer.Sound("/home/pi/python_games/match1.wav")
soundFifteen = pygame.mixer.Sound("/home/pi/python_games/match2.wav")
soundSixteen = pygame.mixer.Sound("/home/pi/python_games/match3.wav")

SoundsList = [soundOne,soundTwo,soundThree,soundFour,soundFive,soundSix,soundSeven,soundEight,soundNine,soundTen,soundEleven,soundTwelve,soundThirteen,soundFourteen,soundFifteen,soundSixteen]

soundChannelOne = pygame.mixer.Channel(1)
soundChannelTwo = pygame.mixer.Channel(2)
soundChannelThree = pygame.mixer.Channel(3)
soundChannelFour = pygame.mixer.Channel(4)
soundChannelFive = pygame.mixer.Channel(5)
soundChannelSix = pygame.mixer.Channel(6)
soundChannelSeven = pygame.mixer.Channel(7)
