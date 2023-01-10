class Stage:

    currentWorld = "grassland"
    currentStage = 1
    saveDropItems = []
    isOpen = False
 
    countMonster = 0
    countKey = 0

    world = {
        "grassland":{

            "stages": {

                "stage 1" : {

                    "name": "Grassland : Stage 1",
                    "description": "",
                    "background": "border: 1px solid black;" "margin: auto;" "background: url(test/images/map/Grassland.png) no-repeat center center;",
                    "monsters": {
                        "name": "Orc",
                        "life": 25,
                        "progressPV": 100,
                        "strength": 50,
                        "defense": 10,
                        "level": 1,
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "front": "background: url(test/sprites/monsters/monster-stage1_front-left.png);" "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);" "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage1_front-left.png);" "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);" "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",                      
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_green-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_green-door.png);"
                    },
                },

                "stage 2" : {

                    "name": "Grassland : Stage 2",
                    "description": "",
                    "background": "",
                    "monsters": {
                        "name": "",
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "front":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_gate.png);",
                        "open_door-image": ""
                    },
                },

                "stage 3" : {

                    "name": "Grassland : Stage 3",
                    "description": "",
                    "background": "",
                    "monsters": {
                        "name": "",
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "front":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_gate.png);",
                        "open_door-image": ""
                    },
                },

                "stage 4" : {

                    "name": "Grassland : Stage 4",
                    "description": "",
                    "background": "",
                    "monsters": {
                        "name": "",
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "front":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_gate.png);",
                        "open_door-image": ""
                    },
                },

                "stage 5" : {

                    "name": "Grassland : Stage final",
                    "description": "",
                    "background": "",
                    "boss": {
                        "name": "",          
                        "info": [],
                        "coordinate" : [],
                        "drop": ["pierre eternel"],
                        "front":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: bottom",
                        "left": "background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",
                        "pierre" : "background: url(test/sprites/monsters/Dead_monster-stage1.png);", 
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_gate.png);",
                        "open_door-image": ""
                    },
                },

            },

        },

        "iceland": {

            "stages": {

                "stage 1" : {

                    "name": "",
                    "description": "",
                    "background": "border: 1px solid black;"  "margin: auto;"  "background: url(test/images/map/IceCave.png) no-repeat center center;",
                    "monsters": {
                        "name": "Slime",
                        "life": 25,
                        "progressPV": 100,
                        "strength": 35,
                        "defense": 10,
                        "level": 1,  
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "front": "background: url(test/sprites/monsters/monster-stage2_front-left.png);" "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage2_right-back.png);" "background-position: bottom",
                        "left": "background: url(test/sprites/monsters/monster-stage2_front-left.png);" "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage2_right-back.png);" "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage2.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage2.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_gate.png);",
                        "open_door-image": ""
                    },
                },

                "stage 2" : {

                    "name": "",
                    "description": "",
                    "background": "",
                    "monsters": {
                        "name": "",
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "front":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_gate.png);",
                        "open_door-image": ""
                    },
                },

                "stage 3" : {

                    "name": "",
                    "description": "",
                    "background": "",
                    "monsters": {
                        "name": "",
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "front":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_gate.png);",
                        "open_door-image": ""
                    },
                },

                "stage 4" : {

                    "name": "",
                    "description": "",
                    "background": "",
                    "monsters": {
                        "name": "",
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "front":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_gate.png);",
                        "open_door-image": ""
                    },
                },

                "stage 5" : {

                    "name": "",
                    "description": "",
                    "background": "",
                    "boss": {
                        "name": "",          
                        "info": [],
                        "coordinate" : [],
                        "drop": ["pierre eternel"],
                        "front":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",
                        "pierre" : "background: url(test/sprites/monsters/Dead_monster-stage1.png);", 
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_gate.png);",
                        "open_door-image": ""
                    },
                },
            },
        },
        
        "lavaland": {

            "stages": {

                "stage 1" : {

                    "name": "",
                    "description": "",
                    "background": "border: 1px solid black;"  "margin: auto;"  "background: url(test/images/map/Lava2.png) no-repeat center center;",
                    "monsters": {
                        "name": "Chimère",
                        "life": 25,
                        "progressPV": 100,
                        "strength": 35,
                        "defense": 10,
                        "level": 1,                      
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "front":"background: url(test/sprites/monsters/monster-stage3_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage3_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage3_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage3_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage3.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage3.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_gate.png);",
                        "open_door-image": ""
                    },
                },

                "stage 2" : {

                    "name": "",
                    "description": "",
                    "background": "",
                    "monsters": {
                        "name": "",
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "front":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_gate.png);",
                        "open_door-image": ""
                    },
                },

                "stage 3" : {

                    "name": "",
                    "description": "",
                    "background": "",
                    "monsters": {
                        "name": "",
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "front":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_gate.png);",
                        "open_door-image": ""
                    },
                },

                "stage 4" : {

                    "name": "",
                    "description": "",
                    "background": "",
                    "monsters": {
                        "name": "",
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "front":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_gate.png);",
                        "open_door-image": ""
                    },
                },

                "stage 5" : {

                    "name": "",
                    "description": "",
                    "background": "",
                    "boss": {
                        "name": "",          
                        "info": [],
                        "coordinate" : [],
                        "drop": ["pierre eternel"],
                        "front":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",
                        "pierre" : "background: url(test/sprites/monsters/Dead_monster-stage1.png);", 
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_gate.png);",
                        "open_door-image": ""
                    },
                },
            },
        },
        
        "cloudland": {

            "stages": {

                "stage 1" : {

                    "name": "",
                    "description": "",
                    "background": "border: 1px solid black;"  "margin: auto;"  "background: url(test/images/map/Clouds.png) no-repeat center center;",
                    "monsters": {
                        "name": "Chien-Dragon",
                        "life": 25,
                        "progressPV": 100,
                        "strength": 35,
                        "defense": 10,
                        "level": 1,                      
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "front":"background: url(test/sprites/monsters/monster-stage4_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage4_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage4_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage4_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage4.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage4.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_gate.png);",
                        "open_door-image": ""
                    },
                },

                "stage 2" : {

                    "name": "",
                    "description": "",
                    "background": "",
                    "monsters": {
                        "name": "",
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "front":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_gate.png);",
                        "open_door-image": ""
                    },
                },

                "stage 3" : {

                    "name": "",
                    "description": "",
                    "background": "",
                    "monsters": {
                        "name": "",
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "front":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_gate.png);",
                        "open_door-image": ""
                    },
                },

                "stage 4" : {

                    "name": "",
                    "description": "",
                    "background": "",
                    "monsters": {
                        "name": "",
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "front":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_gate.png);",
                        "open_door-image": ""
                    },
                },

                "stage 5" : {

                    "name": "",
                    "description": "",
                    "background": "",
                    "boss": {
                        "name": "",          
                        "info": [],
                        "coordinate" : [],
                        "drop": ["pierre eternel"],
                        "front":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",
                        "pierre" : "background: url(test/sprites/monsters/Dead_monster-stage1.png);", 
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_gate.png);",
                        "open_door-image": ""
                    },
                },
            },
        },
        
        "demonicland": {

            "stages": {

                "stage 1" : {

                    "name": "",
                    "description": "",
                    "background": "border: 1px solid black;"  "margin: auto;"  "background: url(test/images/map/DemonicWorld.png) no-repeat center center;",
                    "monsters": {
                        "name": "Diablotin",
                        "life": 25,
                        "progressPV": 100,
                        "strength": 35,
                        "defense": 10,
                        "level": 1,                      
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "front":"background: url(test/sprites/monsters/monster-stage5_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage5_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage5_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage5_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage5.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage5.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_gate.png);",
                        "open_door-image": ""
                    },
                },

                "stage 2" : {

                    "name": "",
                    "description": "",
                    "background": "",
                    "monsters": {
                        "name": "",
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "front":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_gate.png);",
                        "open_door-image": ""
                    },
                },

                "stage 3" : {

                    "name": "",
                    "description": "",
                    "background": "",
                    "monsters": {
                        "name": "",
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "front":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_gate.png);",
                        "open_door-image": ""
                    },
                },

                "stage 4" : {

                    "name": "",
                    "description": "",
                    "background": "",
                    "monsters": {
                        "name": "",
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "front":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_gate.png);",
                        "open_door-image": ""
                    },
                },

                "stage 5" : {

                    "name": "",
                    "description": "",
                    "background": "",
                    "boss": {
                        "name": "",          
                        "info": [],
                        "coordinate" : [],
                        "drop": ["pierre eternel"],
                        "front":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",
                        "pierre" : "background: url(test/sprites/monsters/Dead_monster-stage1.png);", 
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_gate.png);",
                        "open_door-image": ""
                    },
                },
            },
        }
    }

    dropInfo = {
        "petite potion de hp": {
            "description": "",
            "image": "border-image: url(test/sprites/items/hp_potion.png) 0 0 0 0 no-repeat streach streach;" 
        },
        "petit bouclier": {
            "description": "",
            "image": "border-image: url(test/sprites/items/petit_bouclier.png) 0 0 0 0 no-repeat streach streach;"
        },
        "clée du donjon": {
            "description": "",
            "image": "border-image: url(test/sprites/items/dunjon_key.png) 0 0 0 0 no-repeat streach streach;"
        }

    }
