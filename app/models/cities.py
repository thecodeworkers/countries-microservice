from mongoengine import Document, ReferenceField, StringField
from ..utils import RefQuerySet
from bson.json_util import dumps
class Cities(Document):
	state = ReferenceField('States', dbref=False)
	name = StringField(min_length=2, max_length=100, required=True)

	meta = {'queryset_class': RefQuerySet}
	def to_json(self):

		data = self._data
		for key in data:
			if key == 'state':
				data[key] = str(data[key].id)

		data['_id'] = data['id']
		del data['id']

		return dumps(data)
