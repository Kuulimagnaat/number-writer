def eemalda_nullid(sisestus):
    kontrolling = True
    while kontrolling:
        try:
            if sisestus[0] == "0":
                sisestus = sisestus[1:]
            else:
                kontrolling = False
        except IndexError:
            sisestus = "0"
            kontrolling = False
    return sisestus


def sadade_kirjutaja(numbrite_nimed, sisestus):
    if sisestus[0] == "1":
        tulemus = "sada "
    else:
        tulemus = numbrite_nimed[sisestus[0]] + "sada "
    return tulemus


def kahekohaliste_kirjutaja(numbrite_nimed, number):
    if len(number) == 1:
        tulemus = numbrite_nimed[number]
    else:
        number = eemalda_nullid(number)
        if len(number) == 2:
            if number[0] == "1":
                if number[1] == "0":
                    tulemus = "kümme"
                else:
                    tulemus = numbrite_nimed[number[1]] + "teist"
            else:
                if number[1] == "0":
                    tulemus = numbrite_nimed[number[0]] + "kümmend"
                else:
                    tulemus = numbrite_nimed[number[0]] + "kümmend " + numbrite_nimed[number[1]]
        else:
            tulemus = numbrite_nimed[number]
    return tulemus


def kolmekohalise_kirjutaja(numbrite_nimed, sisestus):
    sisestus = eemalda_nullid(sisestus)
    if len(sisestus) == 3:
        output = sadade_kirjutaja(numbrite_nimed, sisestus)
        if sisestus[1:] != "00":
            output += kahekohaliste_kirjutaja(numbrite_nimed, sisestus[1:])
        else:
            pass
    else:
        output = kahekohaliste_kirjutaja(numbrite_nimed, sisestus)
    return output


def suured_arvud(numbrite_nimed, tuhatkohad, sisestus):
    sisestus = eemalda_nullid(sisestus)
    pikkus = len(sisestus)
    j44k = pikkus % 3
    if j44k == 0:
        esimene_arv = sisestus[:3]
        indeks = pikkus//3 - 1
        if esimene_arv == "1":
            tuhatkoht = tuhatkohad[0][indeks]
        else:
            tuhatkoht = tuhatkohad[1][indeks]
    else:
        esimene_arv = sisestus[:j44k]
        indeks = pikkus // 3
        if esimene_arv == "1":
            tuhatkoht = tuhatkohad[0][indeks]
        else:
            tuhatkoht = tuhatkohad[1][indeks]
    output = kolmekohalise_kirjutaja(numbrite_nimed, esimene_arv) + tuhatkoht
    sisestus = sisestus[len(esimene_arv):]

    return output, sisestus


def kordaja(sisestus):
    output = ""
    numbrite_nimed = {
        "0": "null",
        "1": "üks",
        "2": "kaks",
        "3": "kolm",
        "4": "neli",
        "5": "viis",
        "6": "kuus",
        "7": "seitse",
        "8": "kaheksa",
        "9": "üheksa"
    }
    tuhatkohad_ainsus = {
        0: "",
        1: " tuhat ",
        2: " miljon ",
        3: " miljard ",
        4: " triljon ",
        5: " kvadriljon ",
        6: " kvintiljon ",
        7: " sekstiljon ",
        8: " septiljon ",
        9: " oktiljon ",
        10: " noniljon ",
        11: " detsiljon "
    }
    tuhatkohad_mitmus = {
        0: "",
        1: " tuhat ",
        2: " miljonit ",
        3: " miljardit ",
        4: " triljonit ",
        5: " kvadriljonit ",
        6: " kvintiljonit ",
        7: " sekstiljonit ",
        8: " septiljonit ",
        9: " oktiljonit ",
        10: " noniljonit ",
        11: " detsiljonit "
    }
    tuhatkohad = [tuhatkohad_ainsus, tuhatkohad_mitmus]
    while len(sisestus) > 3:
        tulemus, sisestus = suured_arvud(numbrite_nimed, tuhatkohad, sisestus)
        output += tulemus
    else:
        tulemus = kolmekohalise_kirjutaja(numbrite_nimed, sisestus)
        output += tulemus
    return output


def main():
    running = True


    while running:
        sisestus = input(">> ")
        try:
            int(sisestus)
            try:
                output = kordaja(sisestus)
                if output != "null":
                    kontroll = True
                    while kontroll:
                        indeks = output.find("null", len(output) - 7)
                        if indeks == -1:
                            break
                        else:
                            output = output[:indeks]
            except KeyError:
                if eemalda_nullid(sisestus) == "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000":
                    output = "googol"
                else:
                    output = "Ainus millega selle arvu suurus on võrreldav, on Kaarli munn. Seda arvu pole võimalik sõnadega kirjeldada."

        except ValueError:
            output = "See pole number BRUH"
        print(output)


if __name__ == '__main__':
    main()