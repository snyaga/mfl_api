import pydoc

from django.conf import settings
from django.apps import apps


def created_index_inelastic_search():
    """
    The index name will be located in settings
    """


def check_if_elastic_is_running():
    pass


def clear_index():
    pass


def updated_index():
    pass


def purge_index():
    pass


def serialize_model(obj):
    """
    Locates a models serializer and uses it to serializer a model instane
    This allows us to search a document through all its important components.
    If a attribute of model is important enough to appear in the serializer,
    it means that the models should also be searched though that attribute
    as well. This will take care for all the child models of a model if
    they have been inlined in the serializer.

    For this to work a model's serializer name should follow this convention
    '<model_name>Serializer'

    Only apps in local apps will be indexed.
    """
    app_label = obj._meta.app_label
    serializer_path = "{}{}{}{}".format(
        app_label, ".serializers.", obj.__class__.__name__, 'Serializer')
    serializer_cls = pydoc.locate(serializer_path)
    serialized_data = serializer_cls(obj).data
    return {
        "data": serialized_data,
        "index_type": obj.__class__.__name__.lower(),
        "id": str(obj.id)
    }



def index_instance(serialized_obj):
    pass


def failure_queues():
    pass


def process_failure_queue():
    pass


def index_in_realtime():
    pass


def index_periodically():
    pass


def get_document_from_index():
    pass


def search_document_in_index():
    pass
