from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction

from src.functions import generate_synTerms
from src.items import no_input_item, show_suggestion_items


class DictCcExtension(Extension):

    def __init__(self):
        super(DictCcExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        query = event.get_argument() or str()

        # if there is no search term
        if len(query.strip()) == 0:
            return RenderResultListAction(no_input_item())

        # else
        return RenderResultListAction(
            show_suggestion_items(
                [query] + generate_synTerms(query)
            )
        )


if __name__ == '__main__':
    DictCcExtension().run()
