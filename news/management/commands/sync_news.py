# coding=UTF-8
from django.core.management.base import BaseCommand, CommandError
from news.models import Source

class Command(BaseCommand):
	"""
	同步新闻
	"""

	def handle(self, *args, **options):
		sources = Source.objects.filter(active=True, running=False)
		for source in sources:
			num = source.sync()
			self.stdout.write(u"从 %s 同步 %d 条新闻" % (source.key, num))