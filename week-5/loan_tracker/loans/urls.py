from django.urls import path
from .models import Loan
from .views import LoanListView, LoanCreateView, LoanDeleteView, LoanUpdateView

urlpatterns = [
    path('', LoanListView.as_view(), name='loan_list'),
    path('new/', LoanCreateView.as_view(), name='loan_create'),
    path('<int:pk>/edit/', LoanUpdateView.as_view(), name='loan_update'),
    path('<int:pk>/delete/', LoanDeleteView.as_view(), name='loan_delete'),
]
