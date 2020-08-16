from google.protobuf.json_format import MessageToDict
from mongoengine.queryset import NotUniqueError
from ...protos import state_pb2, state_pb2_grpc
from ...utils import parser_all_object, parser_one_object, not_exist_code, exist_code, paginate
from ..bootstrap import grpc_server
from ...models import States


class StateService(state_pb2_grpc.StateServicer):
    def table(self, request, context):
        states = States.objects

        response = paginate(states, request.page, request.per_page)
    
        response = state_pb2.StateTableResponse(**response)
    
        return response
        #try:
        #    
        #except Exception as error:
        #    raise Exception(error)
        

    def get_all(self, request, context):
        states = parser_all_object(States.objects.all())
        response = state_pb2.StateMultipleResponse(language=states)

        return response

    def get(self, request, context):
        try:
            state = States.objects.get(id=request.id)
            state = parser_one_object(state)
            response = state_pb2.StateResponse(language=state)

            return response

        except States.DoesNotExist as e:
            not_exist_code(context, e)

    def save(self, request, context):
        try:
            language_object = MessageToDict(request)
            language = States(**language_object).save()
            language = parser_one_object(language)
            response = state_pb2.StateResponse(language=language)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def update(self, request, context):
        try:
            state_object = MessageToDict(request)
            state = States.objects(id=state_object['id'])

            if not state:
                del state_object['id']

            state = States(**state_object).save()
            state = parser_one_object(state)
            response = state_pb2.StateResponse(language=state)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def delete(self, request, context):
        try:
            state = States.objects.get(id=request.id)
            state = state.delete()
            response = state_pb2.StateEmpty()

            return response

        except States.DoesNotExist as e:
            not_exist_code(context, e)


def start_state_service():
    state_pb2_grpc.add_StateServicer_to_server(StateService(), grpc_server)
