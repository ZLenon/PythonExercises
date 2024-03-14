from time import sleep


market_2nd = {"ns": "green", "ew": "red"}
mission_16th = {"ns": "red", "ew": "green"}


def switchLights(luzes=dict):
    for key in luzes.keys():
        if luzes[key] == "green":
            luzes[key] = "yellow"
            print(luzes[key])
        elif luzes[key] == "yellow":
            luzes[key] = "red"
            print(luzes[key])
        elif luzes[key] == "red":
            luzes[key] = "green"
            print(luzes[key])
    assert "red" in luzes.values(), "Nenhuma das luzes é vermelha! " + str(luzes)

    # chama a função varias vezes
    sleep(2)
    switchLights(luzes)


print(switchLights(market_2nd))
