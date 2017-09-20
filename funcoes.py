#coding=utf-8

def menu_team():
    menu = ('Times responsáveis pelos clientes:\n'
            +'1 - #TeamDelta\n'
            + '2 - #Team Moip\n'
            + '3 - #Team Nextel\n'
            + '4 - #TeamCurvadeRio\n'
            + '5 - #TeamRussia\n'
            + '6 - #tx-noc-Rivendel\n'
            + '7 - #Team Teste')
    return menu

def menu_folders(team_id):
    menu = {1:'Clientes #TeamDelta:\n1 - Caçula dos pneus\n2 - Catraca Livre\n3 - eFácilPlus\n4 - GiulianaFlores\n5 - Gupy\n6 - Kickante\n7 - Navegue Temporada\n8 - Oppa\n9 - Órama\n10 - TBL\n11 - Tarde Force',
            2:'Clientes #Team Moip:\n1 - Moip',
            3:'Clientes #Team Nextel:\n1 - Nextel',
            4:'Clientes #TeamCurvadeRio:\n1 - Printi\n2 - QEdu\n3 - ReclameAqui\n4 - Uplexis',
            5:'Clientes #TeamRussia:\n1 - Ajinomoto\n2 - Arquivei\n3 - Convenia\n4 - Ekkos\n5 - Evino\n6 - FCL - Fundação Casper Libero\n7 - Koin\n8 - MaxMilhas\n9 - Meu Câmbio\n10 - Onawa\n11 - Zooper',
            6:'Clientes #tx-noc-Rivendel:\n1 - Eduk\n2 - Kitado\n3 - Madeira Madeira\n4 - Monkey ECX\n5 - OLX',
            7:'Clientes #Team Teste:\n1 - Teste'}
    return (menu[int(team_id)])

def id_folders(team_id, client_id):
    teamDelta = {1:'0B2jR4SwD34YFVG1PUFpmVjVfS2M', 2:'0B-Ua_mp1P8HzMmJ1OVA1WjlUclk', 3:'0B2jR4SwD34YFX0M4ZmdPaFBGbFU', 4:'0B2jR4SwD34YFZHFxcVFJQkZBUzQ', 5:'0B2jR4SwD34YFS1FKeW8zVUdERms', 6:'0B2jR4SwD34YFUV9LdlREMmlhMkE', 7:'0B-Ua_mp1P8HzVDA4eUNmV09CRjA', 8:'0B2jR4SwD34YFOGRZdXBjUjl5d00', 9:'0B2jR4SwD34YFNDlLd0I5YlZwZFU', 10:'0B2jR4SwD34YFTDYxQldKN0kwRDQ', 11:'0B-Ua_mp1P8HzM2JuMEJvYUFPLVE'}
    teamMoip = {1:'0B-Ua_mp1P8HzV0N0bzB2Y2JIc0U'}
    teamNextel = {1:'0B-Ua_mp1P8HzSTRVVDdXQXpSMlk'}
    teamCurvadeRio = {1:'0ByKnxiRJMMfRNjZqTlNEd192T3c', 2:'0ByKnxiRJMMfRdzNJSXZkNVlOQlE', 3:'0ByKnxiRJMMfRdjlGMW4tSXVZclU', 4:'0B-Ua_mp1P8HzMHB6UkdqeURrNk0'}
    teamRussia = {1:'0B-Ua_mp1P8HzRVFKODFFcEdWbWs', 2:'0BwvFQLAq1SJkNWxZTTNpemdiekU', 3:'0ByKnxiRJMMfRV1BibmhhZHl2UFE', 4:'0ByKnxiRJMMfRY3JMbjJNZnl4REU', 5:'0ByKnxiRJMMfRSmcxMDRkaGFiR0U', 6:'0BwvFQLAq1SJkcGxIc1p5N3ZXWjA', 7:'0ByKnxiRJMMfRRUt2X0dVc1hEOWs', 8:'0ByKnxiRJMMfRd3NhOWs5bl9xSlU', 9:'0ByKnxiRJMMfRdU1wUlVaYnJqVjA', 10:'0B-Ua_mp1P8HzUHNvVDhZaXp3Zmc', 11:'0B-Ua_mp1P8Hzek1nUlZBMXFNOTA'}
    txNocRivendel = {1:'0B16gk9EXIRS5aWtaaUxPSkc1TkU', 2:'0B16gk9EXIRS5ZHFTZlo2Q1NLY28', 3:'0B16gk9EXIRS5cmxfdzh4aUVFS2M', 4:'0ByKnxiRJMMfRZDZqNlQ5ZEc3d0E', 5:'0B16gk9EXIRS5WTJsNFV5dGFicmM'}
    teamTeste = {1:'0B-Ua_mp1P8HzWEVxV3hDdlV0ams'}

    teams = {1:teamDelta, 2:teamMoip, 3:teamNextel, 4:teamCurvadeRio, 5:teamRussia, 6:txNocRivendel, 7:teamTeste}

    return ((teams[int(team_id)])[int(client_id)])
