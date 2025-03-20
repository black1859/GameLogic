from gamelogic.PlayerLogic import Player, getUser
import textManager

p = getUser()
bestHealText = textManager.getBasicReader('events')

# if u use radom, maybe, u can make various game. maybe..
# anyway, after long times, Finally you made game Logic.
# u made player ,Item, text manager, method how can you manage or save player data.
# in cpp for unreal Engine, I hope it was helpful.
def itemDics():
    from gamelogic.ItemLogic import Item,Healpack
    items = {
        1 : Healpack(1), #bestHealpack
        2 : Healpack(2), #wrostHealpack
    }
    #이러면 자동으로 copy가 만들어지네!
    return items

items = itemDics()

def get_besthealpack():
    print(bestHealText.data['best'])
    p.getItem(item = items[1])


def get_wrosthealpack():
    print(bestHealText.data['worst'])
    p.getItem(item = items[2])