FROM python:3.10-alpine AS builder
WORKDIR /rtc2
COPY . .
RUN pip install -r requirements.txt

FROM python:3.10-alpine AS final
COPY --from=builder /rtc2 /rtc2

WORKDIR /rtc2
RUN pip install -r requirements.txt
EXPOSE 5001
CMD ["python", "app.py"]