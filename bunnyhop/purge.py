from bunnyhop.base import BaseBunny


class Purge(BaseBunny):

    def create(self, url):
        response = self.call_api(f"/purge", "POST", params={'url': url})
        if type(response) is bytes:
            return "Purge Queue was finished."
        return response