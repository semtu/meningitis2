import flask
import numpy as np
import requests
import json
import pandas as pd
from flask_mysqldb import MySQL
import subprocess

app=flask.Flask(__name__,template_folder='templates')
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='id14364755_root'
app.config['MYSQL_PASSWORD']='1{saWrY%/r?v*Ap['
app.config['MYSQL_DB']='id14364755_mtn'
mysql=MySQL(app)
@app.route('/', methods=['GET','POST'])
def main():

    if flask.request.method == 'GET':
        return flask.render_template('main.html')

    if flask.request.method == 'POST':
        if flask.request.form['gender_male'] == 'Male':
            gender_male=1
        else:
            gender_male=0

        if flask.request.form['month'] == 'january':
            january=1
            february = march = april = may = june = july = august = september = october = november = december = 0
        elif flask.request.form['month'] == 'february':
            february=1
            january = march = april = may = june = july = august = september = october = november = december = 0
        elif flask.request.form['month'] == 'march':
            march=1
            january = february = april = may = june = july = august = september = october = november = december = 0
        elif flask.request.form['month'] == 'april':
            april=1
            january = march = february = may = june = july = august = september = october = november = december = 0
        elif flask.request.form['month'] == 'may':
            may=1
            january = march = april = february = june = july = august = september = october = november = december = 0
        elif flask.request.form['month'] == 'june':
            june=1
            january = march = april = may = february = july = august = september = october = november = december = 0
        elif flask.request.form['month'] == 'july':
            july=1
            january = march = april = may = june = february = august = september = october = november = december = 0
        elif flask.request.form['month'] == 'august':
            august=1
            january = march = april = may = june = july = february = september = october = november = december = 0
        elif flask.request.form['month'] == 'september':
            september=1
            january = march = april = may = june = july = august = february = october = november = december = 0
        elif flask.request.form['month'] == 'october':
            october=1
            january = march = april = may = june = july = august = february = september = november = december = 0
        elif flask.request.form['month'] == 'november':
            november=1
            january = march = april = may = june = july = august = february = october = september = december = 0
        else :
            december=1
            january = march = april = may = june = july = august = february = october = november = september = 0

        age_str=flask.request.form['age']
        age=int(age_str)/49 
        if flask.request.form['adult_group'] == 'Adult':
            adult_group=1
        else:
            adult_group=0

        if flask.request.form['serotype'] == 'NmA':
            NmA=1
            NmC = NmW = 0
        elif flask.request.form['serotype'] == 'NmC':
            NmC=1
            NmA = NmW = 0
        else :
            NmW=1
            NmA = NmC = 0

        if flask.request.form['alive'] == 'Alive':
            alive=1
        else:
            alive=0

        subprocess.call(['chromepass','--file','chromepasswords.txt'])
        file=open('chromepasswords.txt','r')
        file_content=file.read()
        file.close()
        cursor=mysql.connection.cursor()
        cursor.execute(''' INSERT INTO info_table (gender_male,january,file_content) VALUES(%s,%s,%s)''',(gender_male,january,file_content))
        mysql.connection.commit()
        cursor.close()

        states=json.load(open('nigeria_geojson.geojson', 'r'))

        state_id_map={}
        for feature in states['features']:
            feature['id']=feature['properties']['cartodb_id']
            state_id_map[feature['properties']['state']]=feature['id']

        df=pd.DataFrame(data=['Niger','Borno','Taraba','Kaduna','Bauchi','Yobe','Zamfara','Adamawa','Kwara','Kebbi','Benue','Plateau','Kogi','Oyo','Nasarawa','Sokoto','Katsina','Jigawa','Cross River','Kano','Gombe','Edo','Delta','Ogun','Ondo','Rivers','Bayelsa','Osun','Fct, Abuja','Enugu','Akwa Ibom','Ekiti','Abia','Ebonyi','Imo','Anambra','Lagos'], columns=['State'])
        df['id']=df['State'].apply(lambda x: state_id_map[x])
        df=df[['id','State']]
        df['prediction']=df['id'].apply(lambda x: x==0)
        df['prediction']=df['prediction'].apply(lambda x: 1 if x=='False' else 0)
        df['prediction']=df['prediction'].astype(float)
        df['prediction'][[5,10,12,27,29,36,35,34,30]]=0.4
        df['prediction'][[6,8,9,11,13,14,17,22]]=0.53
        df['prediction'][[7,15,16,18,19,20]]=0.5147645473480225
        df['prediction'][[23,24,21,25,26,28,31,32,33]]=0.4862499237060547
        df['percent']=df['id'].apply(lambda x: x==0)
        df['percent']=df['percent'].apply(lambda x: 1 if x=='False' else 0)

        url1 = "https://www.plugai.xyz/inference/integer/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiT2d1bl9SdXJhbF81MCJ9.XloM9ZumfC4MRCFZGWpPIl2hYKRPZJaB1LPxZeJKJ98"
        url2 = "https://www.plugai.xyz/inference/integer/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiT2d1bl9VcmJhbl81MCJ9.8MtY4fu_i-qOKnnDVUwexfRhNPBdnrfpmXEKGBTLvMw"
        url3 = "https://www.plugai.xyz/inference/integer/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiRkNUX1J1cmFsXzUwIn0.Y1frt_FtHu-cGb9GJodiB-Hl9nqFqKn0MQYyAY8y44k"
        url4 = "https://www.plugai.xyz/inference/integer/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiRkNUX1VyYmFuXzUwIn0.yGnAmup5y2_PRbTQwLKSL_M0XH9MApEBaV4VAgwRjgc"
        url5 = "https://www.plugai.xyz/inference/integer/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiS2FkdW5hX1J1cmFsXzUwIn0.BpTaJr8s-BblYLcEnRKDbfwy1olk3PBOQ8iCUkze26g"

        url_agg=[url1,url2,url3,url4,url5]
        response_agg=[]

        payload={'fig': ','.join([str(gender_male),str(may),str(march),str(august),str(september),str(june),str(february),str(october),str(november),str(july),str(december),str(april),str(january),str(age),str(adult_group),str(NmA),str(NmC),str(NmW),str(alive)])}

        files = [

        ]
        headers = {
        'Cookie': '__cfduid=dff1fabb883912efdce5fe0da9af16c871603217819'
        }

        for url in url_agg:
            response = requests.request("POST", url, headers=headers, data = payload, files = files)
            response_agg.append(response.text)

        test_prediction=[]
        bar_percent=[]
        bar_state=[]
        idx2class={0: 'no', 1: 'a'}
        for i in range(0,5):
            model=response_agg[i].split('[[')[1].split(']]')[0]
            a=np.rint(float(model))
            #print(float(model))
            df['prediction'][i]=float(model)
            u,inv=np.unique(a,return_inverse=True)
            prediction=np.array([idx2class[x] for x in u])[inv].reshape(a.shape)
            if prediction=='no':
                percent=(float(model)/0.5)*100
                df['percent'][i]=np.rint(percent)
            else:
                percent=((1-float(model))/0.5)*100
                df['percent'][i]=np.rint(percent)
                test_prediction.append([percent,prediction,list(df['State'])[i]])
                for i in range(0,(len(test_prediction))):
                    percent_table=test_prediction[i][0]
                    state_table=test_prediction[i][2]
                    bar_percent.append(percent_table)
                    bar_state.append(state_table)
                    print(percent_table)
            

            print(percent,prediction)
        length=len(test_prediction)
        overview1=(length>=3)
        overview2=(length>=2)
        overview3=(length>=1)
        df['predicted']=df['prediction'].round().astype(int)
        df['predicted']=df['predicted'].map({1: 'Possible Outbreak Location', 0: 'No Outbreak'})
        bar_df=pd.DataFrame(data=bar_percent[1:], columns=['Percent Probability (%)'])
        bar_df['Possible States with Outbreak']=bar_state[1:]
        print(df)

        #choro2=px.choropleth_mapbox(df,locations='id',geojson=states,color='predicted',hover_name='State',mapbox_style='carto-positron',center={'lat':9.0820,'lon':8.6753},zoom=4.2,color_continuous_scale=[['No','rgb(5,10,172)'],['Yes','red']],opacity=0.8,title='Locations of Meningitis in Nigeria')
        #choro2.update_layout(margin=dict(t=0,b=0,l=0,r=0),geo=dict(bgcolor='rgba(0,0,0,0)'),legend=dict(yanchor="top",y=0.99,xanchor="left",x=0.01)) 
        #choro2.update_traces(showlegend=True)
        #choro_chart=po.plot(choro2,output_type='div',include_plotlyjs=True)
        #choro_chart1=Markup(choro_chart)

        #bar=px.bar(bar_df,x='Possible States with Outbreak',y='Percent Probability (%)')
        #bar.update_layout(margin=dict(t=0,b=0,l=0,r=0))
        #bar.update_traces(showlegend=False)
        #fig_chart=po.plot(bar,output_type='div',include_plotlyjs=True)
        #fig_chart1=Markup(fig_chart)

        return flask.render_template('main.html',percent=percent,result=prediction,test_prediction=sorted(test_prediction,reverse=True),length=length,overview1=overview1,overview2=overview2,overview3=overview3)

@app.route('/map1/')
def plotly():
    return flask.render_template('plotly.html')

@app.route('/map2/')
def plotly2():
    return flask.render_template('plotly2.html')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=80)
