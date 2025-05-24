# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import pandas as pd
import matplotlib.pyplot as plt
import os

def shipping_per_warehouse(df):
    plt.figure()
    counts = df['Warehouse_block'].value_counts()
    counts.plot.bar(
        title = 'Shipping per Warehouse',
        xlabel = 'Warehouse block', 
        ylabel = 'Record count',
        color = '#55d',
        fontsize = 8
    )
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig('docs/shipping_per_warehouse.png')

def mode_of_shipment(df):
    plt.figure()
    counts = df['Mode_of_Shipment'].value_counts()
    counts.plot.pie(
        title = 'Mode of Shipment',
        wedgeprops= dict(width = 0.4),
        ylabel = '',
        colors = ['#f36', '#6f3', '#36f']
    )
    plt.savefig('docs/mode_of_shipment.png')

def average_customer_rating(df):
    plt.figure()

    df = df[['Mode_of_Shipment', 'Customer_rating']].groupby('Mode_of_Shipment').describe()
    df.columns = df.columns.droplevel()

    df = df[['mean', 'min', 'max']]

    plt.barh(y = df.index.values, width=df['max'].values - 1, left = df['min'].values, height= 0.9, color = '#ccc', alpha = 0.8)

    colors = ['#cfc' if value >= 3.0 else '#f80' for value in df['mean'].values]

    plt.barh(y = df.index.values, width=df['mean'].values - 1, left = df['min'].values, height= 0.5, color = colors, alpha = 1)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_color('#888')
    plt.gca().spines['bottom'].set_color('#888')

    plt.savefig('docs/average_customer_rating.png')

def weight_distribution(df):
    plt.figure()

    df['Weight_in_gms'].plot.hist(title = 'Shipped Weight Distribution', color = '#f80', edgecolor = '#fff')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig('docs/weight_distribution.png')

def write_html():
    html = """
<!DOCTYPE html>
<html>
    <body>
        <h1>Shipping Dashboard</h1>
        <div>
            <img src= 'docs/shipping_per_warehouse.png'>
            <img src= 'docs/mode_of_shipment.png'>
        </div>
            <img src= 'docs/average_customer_rating.png'>
            <img src= 'docs/weight_distribution.png'>
        <div>
        </div>
    </body>
</html>
    """

    with open('docs/index.html', 'w') as file:
        file.write(html)


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """

    if not os.path.exists('docs'):
        os.mkdir('docs')

    df = pd.read_csv('files/input/shipping-data.csv', index_col= 0)

    shipping_per_warehouse(df)
    mode_of_shipment(df)
    average_customer_rating(df)
    weight_distribution(df)
    write_html()

