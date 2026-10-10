import json,sys
w=json.load(open("parsed/working_text.json",encoding="utf-8"))
a,b=int(sys.argv[1]),int(sys.argv[2])
for x in w["articles"]:
    if a<=x["article"]<=b:
        print(f"\n=== Article {x['article']} — {x['title']} [{x['chapter_id']}{' '+x['section_id'] if x['section_id'] else ''}]")
        for p in x["paragraphs"]:
            print(f"[A{x['article']}.P{p['para_label']}] {p['lead']}")
            for l,t in p["points"]: print(f"    {l} {t}")
