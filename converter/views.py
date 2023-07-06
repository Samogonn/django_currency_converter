from django.shortcuts import render

from .forms import ConverterForm
from .services import convert_currencies


def convert(request):
    form = ConverterForm
    template = "converter/converter.html"

    if request.method == "POST":
        amount = float(request.POST.get("amount"))
        from_currency = request.POST.get("from_currency")
        to_currency = request.POST.get("to_currency")

        result = convert_currencies(amount, from_currency, to_currency)

        return render(
            request,
            template,
            {
                "form": form,
                "amount": amount,
                "from_currency": from_currency,
                "to_currency": to_currency,
                "result": result,
            },
        )

    return render(request, template, {"form": form})
