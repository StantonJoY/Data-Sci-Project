Module(
    body=[
        Expr(
            value=Constant(value='\nThe EU_TAX_MAP dictionary contains a basic Tax Mapping for EU countries. It answers the question:\nfor an X% tax rate in the domestic country, what is the corresponding rate in a foreign EU country?\n\nit takes the form tuple: rate, where\n    (Fiscal Country Code, Domestic Tax Rate, Foreign Country Code): Foreign Tax Rate\n', kind=None),
        ),
        Assign(
            targets=[Name(id='EU_TAX_MAP', ctx=Store())],
            value=Dict(
                keys=[
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='AT', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='BG', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CY', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=15.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='CZ', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DE', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='DK', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='EE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ES', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FI', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=2.1, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='FR', kind=None),
                            Constant(value=5.5, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=24.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='GR', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HR', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=27.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='HU', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=13.5, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=4.8, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IE', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=4.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='IT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LT', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=14.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=17.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=3.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LU', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='LV', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=18.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='MT', kind=None),
                            Constant(value=7.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=21.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='NL', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PL', kind=None),
                            Constant(value=8.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=13.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=23.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='PT', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=19.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RO', kind=None),
                            Constant(value=9.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=12.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=25.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SE', kind=None),
                            Constant(value=6.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=22.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=5.0, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SI', kind=None),
                            Constant(value=9.5, kind=None),
                            Constant(value='SK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=10.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='AT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='BE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='BG', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='CY', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='CZ', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='DE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='DK', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='EE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='ES', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='FI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='FR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='GR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='HR', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='HU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='IE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='IT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='LT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='LU', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='LV', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='MT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='NL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='PL', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='PT', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='RO', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='SE', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='SK', kind=None),
                            Constant(value=20.0, kind=None),
                            Constant(value='SI', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                values=[
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=4.8, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=4.8, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=4.8, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=4.8, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=15.0, kind=None),
                    Constant(value=7.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=10.0, kind=None),
                    Constant(value=5.5, kind=None),
                    Constant(value=13.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=13.5, kind=None),
                    Constant(value=4.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=12.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=9.0, kind=None),
                    Constant(value=8.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=5.0, kind=None),
                    Constant(value=6.0, kind=None),
                    Constant(value=9.5, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=20.0, kind=None),
                    Constant(value=24.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=27.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=22.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=17.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=18.0, kind=None),
                    Constant(value=21.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=23.0, kind=None),
                    Constant(value=19.0, kind=None),
                    Constant(value=25.0, kind=None),
                    Constant(value=22.0, kind=None),
                ],
            ),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
