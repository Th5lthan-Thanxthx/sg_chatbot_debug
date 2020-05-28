## 环境配置
conda create -n sg_yycbot python=3.7
source activate
source deactivate
conda activate sg_yycbot
pip install rasa-x~=0.28.3 --extra-index-url https://pypi.rasa.com/simple -i https://pypi.douban.com/simple
pip install jieba -i https://pypi.douban.com/simple
pip install pandas -i https://pypi.douban.com/simple
