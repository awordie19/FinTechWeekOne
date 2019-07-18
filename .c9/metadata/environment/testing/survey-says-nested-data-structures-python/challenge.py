{"changed":true,"filter":false,"title":"challenge.py","tooltip":"/testing/survey-says-nested-data-structures-python/challenge.py","value":"import database\n\n# All the survey responses are stored in a list called \"people\". (Remember to use dot syntax!)\nfrom database import people\n\n\n\n\n# 1. Print out the name of the first person who responded to the survey\n\nprint(people[0][\"Name\"])\n\n\n\n\n# 2. Print out Brenton's second favorite band\n\nprint(people[7][\"Favorite Bands\"][1])\n\n\n\n# 3. For each person on this list, print out a descriptor of where they live in the form \"____ lives in _____.\"\n\n\n\n# for person in people:\n#     print(str(people[\"Name\"]) + \"lives in \" + str(people[\"State\"]) + \".\")\n    \n# for person in people:\n#     print(person[\"Name\"] + \" lives in \" + person[\"State\"] + \".\")\n    \n\n\n# 4. Print out each person's nickname. Write some control flow that determines whether / how to respond if someone didn't provide a nickname.\n\nfor person in people:\n    if person[\"Nickname\"] == \"\":\n        print(\"Oh! \")\n    else:\n        print(person[\"Nickname\"])\n\n\n# 5. Find the average of the respondents' ages.\n\nsumOfAges = 0\n\nfor entry in people:\n    sumOfAges += entry[\"Age\"]\n    \naverageOfAges = sumOfAges/len(people)\nprint(averageOfAges)\n    \n \n\n# 6. Print out the percentage of respondents who have brownn hair.\n\n\n\n\n# 7. Create two new lists - one for programmers, and one for non programmers.\n#    Sort all the people in the main list into these two more specific lists.\n\n\n\n\n# 8. Iterate over the list in order to figure out how many respondents listed \"The Office\" as one of their favorite shows.\n\n\n\n\n# 9. Print out a list of all the bands that are liked by at least two people.\n#    Pro-tip: some respondents capitalized band names and other respondents did not, so for example, if Panic at the Disco isn't listed, your code isn't accurately reporting your results.\n\n\n\n\n\n# 10. Identify anyone on the list who has no common interests (bands or shows) with anyone else. Print their names.\n","undoManager":{"mark":96,"position":100,"stack":[[{"start":{"row":44,"column":12},"end":{"row":44,"column":13},"action":"remove","lines":["0"],"id":751}],[{"start":{"row":44,"column":12},"end":{"row":44,"column":14},"action":"insert","lines":["[]"],"id":752}],[{"start":{"row":44,"column":13},"end":{"row":44,"column":14},"action":"insert","lines":["0"],"id":753}],[{"start":{"row":44,"column":15},"end":{"row":44,"column":16},"action":"insert","lines":["]"],"id":754}],[{"start":{"row":44,"column":15},"end":{"row":44,"column":16},"action":"remove","lines":["]"],"id":755}],[{"start":{"row":44,"column":15},"end":{"row":44,"column":16},"action":"insert","lines":[" "],"id":756},{"start":{"row":44,"column":16},"end":{"row":44,"column":17},"action":"insert","lines":["_"]}],[{"start":{"row":44,"column":16},"end":{"row":44,"column":17},"action":"remove","lines":["_"],"id":757}],[{"start":{"row":44,"column":16},"end":{"row":44,"column":17},"action":"insert","lines":["+"],"id":758}],[{"start":{"row":44,"column":16},"end":{"row":44,"column":17},"action":"remove","lines":["+"],"id":759},{"start":{"row":44,"column":15},"end":{"row":44,"column":16},"action":"remove","lines":[" "]},{"start":{"row":44,"column":14},"end":{"row":44,"column":15},"action":"remove","lines":["]"]},{"start":{"row":44,"column":13},"end":{"row":44,"column":14},"action":"remove","lines":["0"]},{"start":{"row":44,"column":12},"end":{"row":44,"column":13},"action":"remove","lines":["["]},{"start":{"row":44,"column":11},"end":{"row":44,"column":12},"action":"remove","lines":[" "]}],[{"start":{"row":44,"column":11},"end":{"row":44,"column":12},"action":"insert","lines":["0"],"id":760}],[{"start":{"row":44,"column":12},"end":{"row":44,"column":13},"action":"insert","lines":[" "],"id":761}],[{"start":{"row":44,"column":12},"end":{"row":44,"column":13},"action":"remove","lines":[" "],"id":762},{"start":{"row":44,"column":11},"end":{"row":44,"column":12},"action":"remove","lines":["0"]}],[{"start":{"row":44,"column":11},"end":{"row":44,"column":12},"action":"insert","lines":[" "],"id":763},{"start":{"row":44,"column":12},"end":{"row":44,"column":13},"action":"insert","lines":["0"]}],[{"start":{"row":44,"column":13},"end":{"row":45,"column":0},"action":"insert","lines":["",""],"id":764}],[{"start":{"row":45,"column":0},"end":{"row":46,"column":0},"action":"insert","lines":["",""],"id":765}],[{"start":{"row":45,"column":0},"end":{"row":46,"column":0},"action":"remove","lines":["",""],"id":766}],[{"start":{"row":46,"column":20},"end":{"row":47,"column":0},"action":"insert","lines":["",""],"id":767},{"start":{"row":47,"column":0},"end":{"row":47,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":47,"column":4},"end":{"row":47,"column":5},"action":"insert","lines":["s"],"id":768},{"start":{"row":47,"column":5},"end":{"row":47,"column":6},"action":"insert","lines":["u"]},{"start":{"row":47,"column":6},"end":{"row":47,"column":7},"action":"insert","lines":["m"]},{"start":{"row":47,"column":7},"end":{"row":47,"column":8},"action":"insert","lines":["O"]},{"start":{"row":47,"column":8},"end":{"row":47,"column":9},"action":"insert","lines":["f"]},{"start":{"row":47,"column":9},"end":{"row":47,"column":10},"action":"insert","lines":["A"]},{"start":{"row":47,"column":10},"end":{"row":47,"column":11},"action":"insert","lines":["g"]},{"start":{"row":47,"column":11},"end":{"row":47,"column":12},"action":"insert","lines":["e"]},{"start":{"row":47,"column":12},"end":{"row":47,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":47,"column":13},"end":{"row":47,"column":14},"action":"insert","lines":[" "],"id":769},{"start":{"row":47,"column":14},"end":{"row":47,"column":15},"action":"insert","lines":["="]}],[{"start":{"row":47,"column":15},"end":{"row":47,"column":16},"action":"insert","lines":[" "],"id":770},{"start":{"row":47,"column":16},"end":{"row":47,"column":17},"action":"insert","lines":["e"]},{"start":{"row":47,"column":17},"end":{"row":47,"column":18},"action":"insert","lines":["n"]},{"start":{"row":47,"column":18},"end":{"row":47,"column":19},"action":"insert","lines":["t"]}],[{"start":{"row":47,"column":19},"end":{"row":47,"column":20},"action":"insert","lines":["r"],"id":771},{"start":{"row":47,"column":20},"end":{"row":47,"column":21},"action":"insert","lines":["y"]}],[{"start":{"row":47,"column":21},"end":{"row":47,"column":22},"action":"insert","lines":[" "],"id":772}],[{"start":{"row":47,"column":21},"end":{"row":47,"column":22},"action":"remove","lines":[" "],"id":773}],[{"start":{"row":47,"column":21},"end":{"row":47,"column":23},"action":"insert","lines":["[]"],"id":774}],[{"start":{"row":47,"column":22},"end":{"row":47,"column":23},"action":"insert","lines":["A"],"id":775}],[{"start":{"row":47,"column":22},"end":{"row":47,"column":23},"action":"remove","lines":["A"],"id":776}],[{"start":{"row":47,"column":22},"end":{"row":47,"column":23},"action":"insert","lines":["|"],"id":777}],[{"start":{"row":47,"column":22},"end":{"row":47,"column":23},"action":"remove","lines":["|"],"id":778}],[{"start":{"row":47,"column":22},"end":{"row":47,"column":24},"action":"insert","lines":["\"\""],"id":779}],[{"start":{"row":47,"column":23},"end":{"row":47,"column":24},"action":"insert","lines":["A"],"id":780},{"start":{"row":47,"column":24},"end":{"row":47,"column":25},"action":"insert","lines":["g"]},{"start":{"row":47,"column":25},"end":{"row":47,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":47,"column":26},"end":{"row":47,"column":27},"action":"insert","lines":[" "],"id":781}],[{"start":{"row":47,"column":26},"end":{"row":47,"column":27},"action":"remove","lines":[" "],"id":782}],[{"start":{"row":47,"column":28},"end":{"row":48,"column":0},"action":"insert","lines":["",""],"id":783},{"start":{"row":48,"column":0},"end":{"row":48,"column":4},"action":"insert","lines":["    "]},{"start":{"row":48,"column":4},"end":{"row":48,"column":5},"action":"insert","lines":["a"]},{"start":{"row":48,"column":5},"end":{"row":48,"column":6},"action":"insert","lines":["v"]},{"start":{"row":48,"column":6},"end":{"row":48,"column":7},"action":"insert","lines":["e"]},{"start":{"row":48,"column":7},"end":{"row":48,"column":8},"action":"insert","lines":["r"]},{"start":{"row":48,"column":8},"end":{"row":48,"column":9},"action":"insert","lines":["a"]},{"start":{"row":48,"column":9},"end":{"row":48,"column":10},"action":"insert","lines":["g"]},{"start":{"row":48,"column":10},"end":{"row":48,"column":11},"action":"insert","lines":["e"]}],[{"start":{"row":48,"column":11},"end":{"row":48,"column":12},"action":"insert","lines":[" "],"id":784},{"start":{"row":48,"column":12},"end":{"row":48,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":48,"column":12},"end":{"row":48,"column":13},"action":"remove","lines":["="],"id":785},{"start":{"row":48,"column":11},"end":{"row":48,"column":12},"action":"remove","lines":[" "]}],[{"start":{"row":48,"column":11},"end":{"row":48,"column":12},"action":"insert","lines":["o"],"id":786},{"start":{"row":48,"column":12},"end":{"row":48,"column":13},"action":"insert","lines":["f"]}],[{"start":{"row":48,"column":12},"end":{"row":48,"column":13},"action":"remove","lines":["f"],"id":787},{"start":{"row":48,"column":11},"end":{"row":48,"column":12},"action":"remove","lines":["o"]}],[{"start":{"row":48,"column":11},"end":{"row":48,"column":12},"action":"insert","lines":["O"],"id":788},{"start":{"row":48,"column":12},"end":{"row":48,"column":13},"action":"insert","lines":["F"]}],[{"start":{"row":48,"column":12},"end":{"row":48,"column":13},"action":"remove","lines":["F"],"id":789}],[{"start":{"row":48,"column":12},"end":{"row":48,"column":13},"action":"insert","lines":["f"],"id":790}],[{"start":{"row":48,"column":13},"end":{"row":48,"column":14},"action":"insert","lines":[" "],"id":791}],[{"start":{"row":48,"column":13},"end":{"row":48,"column":14},"action":"remove","lines":[" "],"id":792}],[{"start":{"row":48,"column":13},"end":{"row":48,"column":14},"action":"insert","lines":["A"],"id":793}],[{"start":{"row":48,"column":14},"end":{"row":48,"column":15},"action":"insert","lines":[" "],"id":794}],[{"start":{"row":48,"column":14},"end":{"row":48,"column":15},"action":"remove","lines":[" "],"id":795},{"start":{"row":48,"column":13},"end":{"row":48,"column":14},"action":"remove","lines":["A"]}],[{"start":{"row":48,"column":13},"end":{"row":48,"column":14},"action":"insert","lines":["A"],"id":796},{"start":{"row":48,"column":14},"end":{"row":48,"column":15},"action":"insert","lines":["g"]},{"start":{"row":48,"column":15},"end":{"row":48,"column":16},"action":"insert","lines":["e"]},{"start":{"row":48,"column":16},"end":{"row":48,"column":17},"action":"insert","lines":["s"]}],[{"start":{"row":48,"column":17},"end":{"row":48,"column":18},"action":"insert","lines":[" "],"id":797}],[{"start":{"row":48,"column":17},"end":{"row":48,"column":18},"action":"remove","lines":[" "],"id":798},{"start":{"row":48,"column":16},"end":{"row":48,"column":17},"action":"remove","lines":["s"]}],[{"start":{"row":48,"column":3},"end":{"row":48,"column":16},"action":"remove","lines":[" averageOfAge"],"id":799}],[{"start":{"row":47,"column":14},"end":{"row":47,"column":15},"action":"insert","lines":["+"],"id":800}],[{"start":{"row":47,"column":29},"end":{"row":48,"column":0},"action":"insert","lines":["",""],"id":801},{"start":{"row":48,"column":0},"end":{"row":48,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":48,"column":0},"end":{"row":48,"column":4},"action":"remove","lines":["    "],"id":802},{"start":{"row":48,"column":0},"end":{"row":48,"column":1},"action":"insert","lines":["\\"]}],[{"start":{"row":48,"column":0},"end":{"row":48,"column":1},"action":"remove","lines":["\\"],"id":803}],[{"start":{"row":48,"column":0},"end":{"row":48,"column":1},"action":"insert","lines":["p"],"id":804},{"start":{"row":48,"column":1},"end":{"row":48,"column":2},"action":"insert","lines":["r"]},{"start":{"row":48,"column":2},"end":{"row":48,"column":3},"action":"insert","lines":["i"]}],[{"start":{"row":48,"column":2},"end":{"row":48,"column":3},"action":"remove","lines":["i"],"id":805},{"start":{"row":48,"column":1},"end":{"row":48,"column":2},"action":"remove","lines":["r"]},{"start":{"row":48,"column":0},"end":{"row":48,"column":1},"action":"remove","lines":["p"]}],[{"start":{"row":47,"column":29},"end":{"row":48,"column":0},"action":"remove","lines":["",""],"id":806}],[{"start":{"row":47,"column":29},"end":{"row":48,"column":0},"action":"insert","lines":["",""],"id":807},{"start":{"row":48,"column":0},"end":{"row":48,"column":4},"action":"insert","lines":["    "]},{"start":{"row":48,"column":4},"end":{"row":48,"column":5},"action":"insert","lines":["a"]},{"start":{"row":48,"column":5},"end":{"row":48,"column":6},"action":"insert","lines":["v"]},{"start":{"row":48,"column":6},"end":{"row":48,"column":7},"action":"insert","lines":["e"]},{"start":{"row":48,"column":7},"end":{"row":48,"column":8},"action":"insert","lines":["r"]},{"start":{"row":48,"column":8},"end":{"row":48,"column":9},"action":"insert","lines":["a"]},{"start":{"row":48,"column":9},"end":{"row":48,"column":10},"action":"insert","lines":["g"]},{"start":{"row":48,"column":10},"end":{"row":48,"column":11},"action":"insert","lines":["e"]}],[{"start":{"row":48,"column":11},"end":{"row":48,"column":12},"action":"insert","lines":["o"],"id":808},{"start":{"row":48,"column":12},"end":{"row":48,"column":13},"action":"insert","lines":["f"]}],[{"start":{"row":48,"column":12},"end":{"row":48,"column":13},"action":"remove","lines":["f"],"id":809},{"start":{"row":48,"column":11},"end":{"row":48,"column":12},"action":"remove","lines":["o"]}],[{"start":{"row":48,"column":11},"end":{"row":48,"column":12},"action":"insert","lines":["O"],"id":810},{"start":{"row":48,"column":12},"end":{"row":48,"column":13},"action":"insert","lines":["f"]},{"start":{"row":48,"column":13},"end":{"row":48,"column":14},"action":"insert","lines":["A"]},{"start":{"row":48,"column":14},"end":{"row":48,"column":15},"action":"insert","lines":["g"]},{"start":{"row":48,"column":15},"end":{"row":48,"column":16},"action":"insert","lines":["e"]},{"start":{"row":48,"column":16},"end":{"row":48,"column":17},"action":"insert","lines":["s"]}],[{"start":{"row":48,"column":17},"end":{"row":48,"column":18},"action":"insert","lines":["/"],"id":811}],[{"start":{"row":48,"column":18},"end":{"row":48,"column":19},"action":"insert","lines":[" "],"id":812}],[{"start":{"row":48,"column":18},"end":{"row":48,"column":19},"action":"remove","lines":[" "],"id":813}],[{"start":{"row":48,"column":18},"end":{"row":48,"column":19},"action":"insert","lines":[" "],"id":814}],[{"start":{"row":48,"column":18},"end":{"row":48,"column":19},"action":"remove","lines":[" "],"id":815}],[{"start":{"row":48,"column":18},"end":{"row":48,"column":19},"action":"insert","lines":["2"],"id":816}],[{"start":{"row":48,"column":18},"end":{"row":48,"column":19},"action":"remove","lines":["2"],"id":817},{"start":{"row":48,"column":17},"end":{"row":48,"column":18},"action":"remove","lines":["/"]}],[{"start":{"row":48,"column":17},"end":{"row":48,"column":18},"action":"insert","lines":[" "],"id":818},{"start":{"row":48,"column":18},"end":{"row":48,"column":19},"action":"insert","lines":["="]},{"start":{"row":48,"column":19},"end":{"row":48,"column":20},"action":"insert","lines":["="]}],[{"start":{"row":48,"column":20},"end":{"row":48,"column":21},"action":"insert","lines":[" "],"id":819}],[{"start":{"row":48,"column":20},"end":{"row":48,"column":21},"action":"remove","lines":[" "],"id":820},{"start":{"row":48,"column":19},"end":{"row":48,"column":20},"action":"remove","lines":["="]}],[{"start":{"row":48,"column":19},"end":{"row":48,"column":20},"action":"insert","lines":[" "],"id":821},{"start":{"row":48,"column":20},"end":{"row":48,"column":21},"action":"insert","lines":["d"]}],[{"start":{"row":48,"column":20},"end":{"row":48,"column":21},"action":"remove","lines":["d"],"id":822},{"start":{"row":48,"column":19},"end":{"row":48,"column":20},"action":"remove","lines":[" "]}],[{"start":{"row":48,"column":19},"end":{"row":48,"column":20},"action":"insert","lines":[" "],"id":823},{"start":{"row":48,"column":20},"end":{"row":48,"column":21},"action":"insert","lines":["d"]}],[{"start":{"row":48,"column":20},"end":{"row":48,"column":21},"action":"remove","lines":["d"],"id":824}],[{"start":{"row":48,"column":20},"end":{"row":48,"column":21},"action":"insert","lines":["s"],"id":825},{"start":{"row":48,"column":21},"end":{"row":48,"column":22},"action":"insert","lines":["u"]},{"start":{"row":48,"column":22},"end":{"row":48,"column":23},"action":"insert","lines":["m"]},{"start":{"row":48,"column":23},"end":{"row":48,"column":24},"action":"insert","lines":["O"]},{"start":{"row":48,"column":24},"end":{"row":48,"column":25},"action":"insert","lines":["f"]},{"start":{"row":48,"column":25},"end":{"row":48,"column":26},"action":"insert","lines":["A"]},{"start":{"row":48,"column":26},"end":{"row":48,"column":27},"action":"insert","lines":["g"]}],[{"start":{"row":48,"column":27},"end":{"row":48,"column":28},"action":"insert","lines":["e"],"id":826},{"start":{"row":48,"column":28},"end":{"row":48,"column":29},"action":"insert","lines":["s"]},{"start":{"row":48,"column":29},"end":{"row":48,"column":30},"action":"insert","lines":["/"]},{"start":{"row":48,"column":30},"end":{"row":48,"column":31},"action":"insert","lines":["2"]},{"start":{"row":48,"column":31},"end":{"row":48,"column":32},"action":"insert","lines":["0"]}],[{"start":{"row":50,"column":10},"end":{"row":50,"column":22},"action":"remove","lines":["entry[\"Age\"]"],"id":827}],[{"start":{"row":50,"column":10},"end":{"row":50,"column":11},"action":"insert","lines":["a"],"id":828},{"start":{"row":50,"column":11},"end":{"row":50,"column":12},"action":"insert","lines":["v"]},{"start":{"row":50,"column":12},"end":{"row":50,"column":13},"action":"insert","lines":["e"]},{"start":{"row":50,"column":13},"end":{"row":50,"column":14},"action":"insert","lines":["r"]},{"start":{"row":50,"column":14},"end":{"row":50,"column":15},"action":"insert","lines":["a"]},{"start":{"row":50,"column":15},"end":{"row":50,"column":16},"action":"insert","lines":["g"]},{"start":{"row":50,"column":16},"end":{"row":50,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":50,"column":10},"end":{"row":50,"column":17},"action":"remove","lines":["average"],"id":829},{"start":{"row":50,"column":10},"end":{"row":50,"column":23},"action":"insert","lines":["averageOfAges"]}],[{"start":{"row":49,"column":2},"end":{"row":49,"column":3},"action":"remove","lines":[" "],"id":830},{"start":{"row":49,"column":1},"end":{"row":49,"column":2},"action":"remove","lines":[" "]},{"start":{"row":49,"column":0},"end":{"row":49,"column":1},"action":"remove","lines":[" "]},{"start":{"row":48,"column":32},"end":{"row":49,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":48,"column":0},"end":{"row":48,"column":4},"action":"remove","lines":["    "],"id":831}],[{"start":{"row":47,"column":0},"end":{"row":47,"column":4},"action":"remove","lines":["    "],"id":832}],[{"start":{"row":47,"column":0},"end":{"row":48,"column":0},"action":"insert","lines":["",""],"id":833},{"start":{"row":48,"column":0},"end":{"row":49,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":51,"column":0},"end":{"row":51,"column":4},"action":"remove","lines":["    "],"id":834}],[{"start":{"row":48,"column":0},"end":{"row":49,"column":0},"action":"remove","lines":["",""],"id":835},{"start":{"row":47,"column":0},"end":{"row":48,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":47,"column":0},"end":{"row":47,"column":4},"action":"insert","lines":["    "],"id":836}],[{"start":{"row":47,"column":29},"end":{"row":48,"column":0},"action":"insert","lines":["",""],"id":837},{"start":{"row":48,"column":0},"end":{"row":48,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":52,"column":0},"end":{"row":53,"column":16},"action":"remove","lines":["#     age = int(people[\"Age\"])","#     print(age)"],"id":838},{"start":{"row":51,"column":4},"end":{"row":52,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":49,"column":27},"end":{"row":49,"column":28},"action":"remove","lines":["0"],"id":839},{"start":{"row":49,"column":26},"end":{"row":49,"column":27},"action":"remove","lines":["2"]}],[{"start":{"row":49,"column":26},"end":{"row":49,"column":28},"action":"insert","lines":["()"],"id":840}],[{"start":{"row":49,"column":27},"end":{"row":49,"column":28},"action":"insert","lines":["l"],"id":841}],[{"start":{"row":49,"column":27},"end":{"row":49,"column":28},"action":"remove","lines":["l"],"id":842},{"start":{"row":49,"column":26},"end":{"row":49,"column":28},"action":"remove","lines":["()"]}],[{"start":{"row":49,"column":26},"end":{"row":49,"column":27},"action":"insert","lines":["l"],"id":843},{"start":{"row":49,"column":27},"end":{"row":49,"column":28},"action":"insert","lines":["e"]},{"start":{"row":49,"column":28},"end":{"row":49,"column":29},"action":"insert","lines":["n"]}],[{"start":{"row":49,"column":29},"end":{"row":49,"column":31},"action":"insert","lines":["()"],"id":844}],[{"start":{"row":49,"column":30},"end":{"row":49,"column":31},"action":"insert","lines":["f"],"id":845}],[{"start":{"row":49,"column":30},"end":{"row":49,"column":31},"action":"remove","lines":["f"],"id":846}],[{"start":{"row":49,"column":30},"end":{"row":49,"column":31},"action":"insert","lines":["p"],"id":847},{"start":{"row":49,"column":31},"end":{"row":49,"column":32},"action":"insert","lines":["e"]},{"start":{"row":49,"column":32},"end":{"row":49,"column":33},"action":"insert","lines":["o"]},{"start":{"row":49,"column":33},"end":{"row":49,"column":34},"action":"insert","lines":["p"]},{"start":{"row":49,"column":34},"end":{"row":49,"column":35},"action":"insert","lines":["l"]},{"start":{"row":49,"column":35},"end":{"row":49,"column":36},"action":"insert","lines":["e"]}],[{"start":{"row":51,"column":4},"end":{"row":52,"column":0},"action":"insert","lines":["",""],"id":848},{"start":{"row":52,"column":0},"end":{"row":52,"column":4},"action":"insert","lines":["    "]},{"start":{"row":52,"column":4},"end":{"row":53,"column":0},"action":"insert","lines":["",""]},{"start":{"row":53,"column":0},"end":{"row":53,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":53,"column":0},"end":{"row":53,"column":4},"action":"remove","lines":["    "],"id":849},{"start":{"row":52,"column":4},"end":{"row":53,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":52,"column":4},"end":{"row":52,"column":5},"action":"insert","lines":["\\"],"id":850}],[{"start":{"row":52,"column":4},"end":{"row":52,"column":5},"action":"remove","lines":["\\"],"id":851},{"start":{"row":52,"column":0},"end":{"row":52,"column":4},"action":"remove","lines":["    "]},{"start":{"row":51,"column":4},"end":{"row":52,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":710.5,"scrollleft":0,"selection":{"start":{"row":51,"column":4},"end":{"row":51,"column":4},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1563391083857}