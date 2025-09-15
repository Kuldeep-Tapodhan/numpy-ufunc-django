import numpy as np
from django.shortcuts import render
from django.http import JsonResponse
import json
 
def ufunc_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            array_data = data.get('array_data')
            constant = float(data.get('constant'))
            
            if not array_data:
                raise ValueError("Input array cannot be empty.")
            
            input_list = [float(x.strip()) for x in array_data.split(',') if x.strip()]
            input_array = np.array(input_list, dtype=float)
            
            def my_ufunc_func(x, c):
                return x**2 + c
            
            my_ufunc = np.vectorize(my_ufunc_func)
            
            result_array = my_ufunc(input_array, constant)
            
            return JsonResponse({
                'success': True,
                'input_array': input_array.tolist(),
                'result_array': result_array.tolist(),
                'constant': constant
            })
 
        except (ValueError, json.JSONDecodeError) as e:
            return JsonResponse({'success': False, 'error': str(e)})
        except Exception as e:
            return JsonResponse({'success': False, 'error': f"An unexpected error occurred: {e}"})
 
    return render(request, 'core/ufunc_page.html')