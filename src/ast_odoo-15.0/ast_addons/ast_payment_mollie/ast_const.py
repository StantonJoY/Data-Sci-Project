Module(
    body=[
        Assign(
            targets=[Name(id='SUPPORTED_LOCALES', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='en_US', kind=None),
                    Constant(value='nl_NL', kind=None),
                    Constant(value='nl_BE', kind=None),
                    Constant(value='fr_FR', kind=None),
                    Constant(value='fr_BE', kind=None),
                    Constant(value='de_DE', kind=None),
                    Constant(value='de_AT', kind=None),
                    Constant(value='de_CH', kind=None),
                    Constant(value='es_ES', kind=None),
                    Constant(value='ca_ES', kind=None),
                    Constant(value='pt_PT', kind=None),
                    Constant(value='it_IT', kind=None),
                    Constant(value='nb_NO', kind=None),
                    Constant(value='sv_SE', kind=None),
                    Constant(value='fi_FI', kind=None),
                    Constant(value='da_DK', kind=None),
                    Constant(value='is_IS', kind=None),
                    Constant(value='hu_HU', kind=None),
                    Constant(value='pl_PL', kind=None),
                    Constant(value='lv_LV', kind=None),
                    Constant(value='lt_LT', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='SUPPORTED_CURRENCIES', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='AED', kind=None),
                    Constant(value='AUD', kind=None),
                    Constant(value='BGN', kind=None),
                    Constant(value='BRL', kind=None),
                    Constant(value='CAD', kind=None),
                    Constant(value='CHF', kind=None),
                    Constant(value='CZK', kind=None),
                    Constant(value='DKK', kind=None),
                    Constant(value='EUR', kind=None),
                    Constant(value='GBP', kind=None),
                    Constant(value='HKD', kind=None),
                    Constant(value='HRK', kind=None),
                    Constant(value='HUF', kind=None),
                    Constant(value='ILS', kind=None),
                    Constant(value='ISK', kind=None),
                    Constant(value='JPY', kind=None),
                    Constant(value='MXN', kind=None),
                    Constant(value='MYR', kind=None),
                    Constant(value='NOK', kind=None),
                    Constant(value='NZD', kind=None),
                    Constant(value='PHP', kind=None),
                    Constant(value='PLN', kind=None),
                    Constant(value='RON', kind=None),
                    Constant(value='RUB', kind=None),
                    Constant(value='SEK', kind=None),
                    Constant(value='SGD', kind=None),
                    Constant(value='THB', kind=None),
                    Constant(value='TWD', kind=None),
                    Constant(value='USD', kind=None),
                    Constant(value='ZAR', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)