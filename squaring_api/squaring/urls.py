from django.urls import path
from squaring.views import HelloWorldView,SquaringView


urlpatterns = [
    # squaring/
    # NOTE: in class, the `path` to the HelloWorldView was the word 'home'. Here, it's empty instead.
    # How will that change the way that the user will access this url in the browser or in code?
    path('', HelloWorldView.as_view()),
    path('<int:number>',SquaringView.as_view())
]