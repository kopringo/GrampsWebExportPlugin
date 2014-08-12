import sys, os, pickle
sys.path.append('/home/kopringo/gramps-web-viewer')
os.environ["DJANGO_SETTINGS_MODULE"] = "gramps_web_viewer.settings"
from gramps_web_viewer.libdjango import DjangoInterface

file = open('/tmp/dbg.pkl', 'r')
_database = pickle.load(file)

class Oo:
    person_map = {}
    note_map = {}
    family_map = {}
    event_map = {}
    place_map = {}
    media_map = {}
database = Oo()
database.person_map = _database['person_map']
database.note_map = _database['note_map']
database.family_map = _database['family_map']
database.event_map = _database['event_map']
database.place_map = _database['place_map']
database.media_map = _database['media_map']
dji = DjangoInterface()
for step in [0, 1]:
    print "Exporting Step %d..." % 1
    # ---------------------------------
    # Person
    # ---------------------------------
    for person_handle in database.person_map.keys():
        data = database.person_map[person_handle]
        if step == 0:
            dji.add_person(data)
        elif step == 1:
            pass
            dji.add_person_detail(data)
            #djperson.probably_alive = not bool(djperson.death)
            #djperson.save()
        #count += 1
        #callback(100 * count/total)
        
    # ---------------------------------
    # Family
    # ---------------------------------
    for family_handle in database.family_map.keys():
        data = database.family_map[family_handle]
        if step == 0:
            dji.add_family(data)
        elif step == 1:
            dji.add_family_detail(data)
    
    # ---------------------------------
    # Event
    # ---------------------------------
    for event_handle in database.event_map.keys():
        data = database.event_map[event_handle]
        if step == 0:
            dji.add_event(data)
        elif step == 1:
            dji.add_event_detail(data)
    
    # ---------------------------------
    # Place 
    # ---------------------------------
    for place_handle in database.place_map.keys():
        data = database.place_map[place_handle]
        if step == 0:
            dji.add_place(data)
        elif step == 1:
            dji.add_place_detail(data)
    
    # ---------------------------------
    # Notes
    # ---------------------------------
    """
    for note_handle in database.note_map.keys():
        data = database.note_map[note_handle]
        if step == 0:
            dji.add_note(data)
        count += 1
        callback(100 * count/total)
    """
    
    # ---------------------------------
    # Media
    # ---------------------------------
    """
    for media_handle in database.media_map.keys():
        data = database.media_map[media_handle]
        if step == 0:
            dji.add_media(data)
        elif step == 1:
            dji.add_media_detail(data)
        count += 1
        callback(100 * count/total)
    """