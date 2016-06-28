from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.core.urlresolvers import reverse
from myblog.models import Post

class LatestEntriesFeed(Feed):
	title = "RSS feed from myblog"
	link = "/rss/"
	description = "the most recents posts on myblog"

	def items(self):
		return Post.objects.order_by('-published_date')[:5]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.text

	def item_author_name(self, item):
		return item.author

	def item_pubdate(self, item):
		return item.published_date

	def item_link(self, item):
		return 'http'

class AtomLatestEntriesFeed(LatestEntriesFeed):
	feed_type = Atom1Feed
	subtitle = LatestEntriesFeed.description
