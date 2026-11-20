from rest_framework.routers import DefaultRouter
from books.api import CategoryViewSet, BookViewSet, BookCopyViewSet
from members.api import MemberViewSet
from circulation.api import BorrowRecordViewSet, ReservationViewSet, FineViewSet
router=DefaultRouter()
router.register('categories',CategoryViewSet)
router.register('books',BookViewSet)
router.register('copies',BookCopyViewSet)
router.register('members',MemberViewSet)
router.register('borrow-records',BorrowRecordViewSet)
router.register('reservations',ReservationViewSet)
router.register('fines',FineViewSet)
urlpatterns=router.urls
