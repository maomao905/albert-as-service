## albert-as-service
### install
```sh
git clone https://github.com/maomao905/albert-as-service.git
cd albert-as-service/server
python setup.py install
pip install albert_serving_server[http]
```
### start server
- place your ALBERT model and sentencepiece model in specified directory
```sh
albert-serving-start \
  -num_worker=$NUM_WORKER \
  -max_seq_len=$MAX_SEQ_LEN \
  -model_dir=/opt/models \
  -spm_model_file=/opt/models/spm.model \
  -http_port=8125 \
  -swagger_file_path=/opt/app/bertApi.openapi.yaml
```
### send request
```sh
curl -X POST http://xx.xx.xx.xx:8125/encode \
  -H 'content-type: application/json' \
  -d '{"id": 123,"texts": ["hello world"], "is_tokenized": false}'
```
