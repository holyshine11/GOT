# hotels/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Hotel
from .forms import HotelForm
from django.urls import reverse_lazy
from django.contrib import messages

class HotelListView(ListView):
    model = Hotel
    template_name = 'hotels/hotel_list.html'
    context_object_name = 'hotels'
    paginate_by = 3

    def get_queryset(self):
        query_name = self.request.GET.get('name', '')
        if query_name:
            return Hotel.objects.filter(name__icontains=query_name)
        else:
            return Hotel.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['query_name'] = self.request.GET.get('name', '')
    #     context['hotels'] = self.object_list
    #     return context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query_name'] = self.request.GET.get('name', '')
        return context  # 'hotels' 변수를 설정하지 않습니다.


class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'hotels/hotel_detail.html'
    context_object_name = 'hotel'



class HotelCreateView(View):
    template_name = 'hotels/hotel_create.html'

    def get(self, request):
        form = HotelForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = HotelForm(request.POST, request.FILES)  # 이미지 업로드를 위해 request.FILES 포함
        if form.is_valid():
            form.save()
            messages.success(request, "호텔이 성공적으로 등록되었습니다.")
            return redirect('hotel_list')  # 네임스페이스 없이 URL 이름으로 리다이렉트
        return render(request, self.template_name, {'form': form})


class HotelUpdateView(View):
    template_name = 'hotels/hotel_update.html'

    def get(self, request, pk):
        hotel = get_object_or_404(Hotel, pk=pk)
        form = HotelForm(instance=hotel)
        return render(request, self.template_name, {'form': form, 'hotel': hotel})

    def post(self, request, pk):
        hotel = get_object_or_404(Hotel, pk=pk)
        form = HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            messages.success(request, "호텔 정보가 성공적으로 수정되었습니다.")
            return redirect('hotels:hotel_detail', pk=hotel.pk)
        return render(request, self.template_name, {'form': form, 'hotel': hotel})

class HotelDeleteView(View):
    template_name = 'hotels/hotel_confirm_delete.html'

    def get(self, request, pk):
        hotel = get_object_or_404(Hotel, pk=pk)
        return render(request, self.template_name, {'hotel': hotel})

    def post(self, request, pk):
        hotel = get_object_or_404(Hotel, pk=pk)
        hotel.delete()
        messages.success(request, "호텔이 성공적으로 삭제되었습니다.")
        return redirect('hotels:hotel_list')
