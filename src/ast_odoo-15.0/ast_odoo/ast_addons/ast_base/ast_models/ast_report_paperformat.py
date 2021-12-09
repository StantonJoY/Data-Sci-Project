Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='PAPER_SIZES', ctx=Store())],
            value=List(
                elts=[
                    Dict(
                        keys=[
                            Constant(value='description', kind=None),
                            Constant(value='key', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='A0  5   841 x 1189 mm', kind=None),
                            Constant(value='A0', kind=None),
                            Constant(value=1189.0, kind=None),
                            Constant(value=841.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='A1', kind=None),
                            Constant(value='A1  6   594 x 841 mm', kind=None),
                            Constant(value=841.0, kind=None),
                            Constant(value=594.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='A2', kind=None),
                            Constant(value='A2  7   420 x 594 mm', kind=None),
                            Constant(value=594.0, kind=None),
                            Constant(value=420.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='A3', kind=None),
                            Constant(value='A3  8   297 x 420 mm', kind=None),
                            Constant(value=420.0, kind=None),
                            Constant(value=297.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='A4', kind=None),
                            Constant(value='A4  0   210 x 297 mm, 8.26 x 11.69 inches', kind=None),
                            Constant(value=297.0, kind=None),
                            Constant(value=210.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='A5', kind=None),
                            Constant(value='A5  9   148 x 210 mm', kind=None),
                            Constant(value=210.0, kind=None),
                            Constant(value=148.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='A6', kind=None),
                            Constant(value='A6  10  105 x 148 mm', kind=None),
                            Constant(value=148.0, kind=None),
                            Constant(value=105.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='A7', kind=None),
                            Constant(value='A7  11  74 x 105 mm', kind=None),
                            Constant(value=105.0, kind=None),
                            Constant(value=74.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='A8', kind=None),
                            Constant(value='A8  12  52 x 74 mm', kind=None),
                            Constant(value=74.0, kind=None),
                            Constant(value=52.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='A9', kind=None),
                            Constant(value='A9  13  37 x 52 mm', kind=None),
                            Constant(value=52.0, kind=None),
                            Constant(value=37.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='B0', kind=None),
                            Constant(value='B0  14  1000 x 1414 mm', kind=None),
                            Constant(value=1414.0, kind=None),
                            Constant(value=1000.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='B1', kind=None),
                            Constant(value='B1  15  707 x 1000 mm', kind=None),
                            Constant(value=1000.0, kind=None),
                            Constant(value=707.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='B2', kind=None),
                            Constant(value='B2  17  500 x 707 mm', kind=None),
                            Constant(value=707.0, kind=None),
                            Constant(value=500.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='B3', kind=None),
                            Constant(value='B3  18  353 x 500 mm', kind=None),
                            Constant(value=500.0, kind=None),
                            Constant(value=353.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='B4', kind=None),
                            Constant(value='B4  19  250 x 353 mm', kind=None),
                            Constant(value=353.0, kind=None),
                            Constant(value=250.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='B5', kind=None),
                            Constant(value='B5  1   176 x 250 mm, 6.93 x 9.84 inches', kind=None),
                            Constant(value=250.0, kind=None),
                            Constant(value=176.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='B6', kind=None),
                            Constant(value='B6  20  125 x 176 mm', kind=None),
                            Constant(value=176.0, kind=None),
                            Constant(value=125.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='B7', kind=None),
                            Constant(value='B7  21  88 x 125 mm', kind=None),
                            Constant(value=125.0, kind=None),
                            Constant(value=88.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='B8', kind=None),
                            Constant(value='B8  22  62 x 88 mm', kind=None),
                            Constant(value=88.0, kind=None),
                            Constant(value=62.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='B9', kind=None),
                            Constant(value='B9  23  33 x 62 mm', kind=None),
                            Constant(value=62.0, kind=None),
                            Constant(value=33.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='B10', kind=None),
                            Constant(value='B10    16  31 x 44 mm', kind=None),
                            Constant(value=44.0, kind=None),
                            Constant(value=31.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='C5E', kind=None),
                            Constant(value='C5E 24  163 x 229 mm', kind=None),
                            Constant(value=229.0, kind=None),
                            Constant(value=163.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='Comm10E', kind=None),
                            Constant(value='Comm10E 25  105 x 241 mm, U.S. Common 10 Envelope', kind=None),
                            Constant(value=241.0, kind=None),
                            Constant(value=105.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='DLE', kind=None),
                            Constant(value='DLE 26 110 x 220 mm', kind=None),
                            Constant(value=220.0, kind=None),
                            Constant(value=110.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='Executive', kind=None),
                            Constant(value='Executive 4   7.5 x 10 inches, 190.5 x 254 mm', kind=None),
                            Constant(value=254.0, kind=None),
                            Constant(value=190.5, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='Folio', kind=None),
                            Constant(value='Folio 27  210 x 330 mm', kind=None),
                            Constant(value=330.0, kind=None),
                            Constant(value=210.0, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='Ledger', kind=None),
                            Constant(value='Ledger  28  431.8 x 279.4 mm', kind=None),
                            Constant(value=279.4, kind=None),
                            Constant(value=431.8, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='Legal', kind=None),
                            Constant(value='Legal    3   8.5 x 14 inches, 215.9 x 355.6 mm', kind=None),
                            Constant(value=355.6, kind=None),
                            Constant(value=215.9, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='Letter', kind=None),
                            Constant(value='Letter 2 8.5 x 11 inches, 215.9 x 279.4 mm', kind=None),
                            Constant(value=279.4, kind=None),
                            Constant(value=215.9, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='height', kind=None),
                            Constant(value='width', kind=None),
                        ],
                        values=[
                            Constant(value='Tabloid', kind=None),
                            Constant(value='Tabloid 29 279.4 x 431.8 mm', kind=None),
                            Constant(value=431.8, kind=None),
                            Constant(value=279.4, kind=None),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                        ],
                        values=[
                            Constant(value='custom', kind=None),
                            Constant(value='Custom', kind=None),
                        ],
                    ),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        ClassDef(
            name='report_paperformat',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='report.paperformat', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Paper Format Config', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Name', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='default', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Default paper format ?', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='format', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            ListComp(
                                elt=Tuple(
                                    elts=[
                                        Subscript(
                                            value=Name(id='ps', ctx=Load()),
                                            slice=Constant(value='key', kind=None),
                                            ctx=Load(),
                                        ),
                                        Subscript(
                                            value=Name(id='ps', ctx=Load()),
                                            slice=Constant(value='description', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='ps', ctx=Store()),
                                        iter=Name(id='PAPER_SIZES', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            Constant(value='Paper size', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='A4', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Select Proper Paper size', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='margin_top', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Top Margin (mm)', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=40, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='margin_bottom', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Bottom Margin (mm)', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=20, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='margin_left', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Left Margin (mm)', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=7, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='margin_right', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Right Margin (mm)', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=7, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='page_height', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Page height (mm)', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='page_width', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Page width (mm)', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='orientation', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='Landscape', kind=None),
                                            Constant(value='Landscape', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='Portrait', kind=None),
                                            Constant(value='Portrait', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            Constant(value='Orientation', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='Landscape', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='header_line', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Display a header line', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='header_spacing', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Header spacing', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=35, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='disable_shrinking', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Disable smart shrinking', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='dpi', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Output DPI', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=90, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='report_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='ir.actions.report', kind=None),
                            Constant(value='paperformat_id', kind=None),
                            Constant(value='Associated reports', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Explicitly associated reports', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='print_page_width', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Print page width (mm)', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_print_page_size', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='print_page_height', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Print page height (mm)', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_print_page_size', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_format_or_page',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='x', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='x', ctx=Load()),
                                                        attr='format',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[NotEq()],
                                                    comparators=[Constant(value='custom', kind=None)],
                                                ),
                                                BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Attribute(
                                                            value=Name(id='x', ctx=Load()),
                                                            attr='page_width',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='x', ctx=Load()),
                                                            attr='page_height',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='You can select either a format or a specific page width/height, but not both.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[Constant(value='format', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_print_page_size',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='width', ctx=Store()),
                                        Name(id='height', ctx=Store()),
                                    ],
                                    value=Constant(value=0.0, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='format',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='format',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='custom', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='width', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='page_width',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='height', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='page_height',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='paper_size', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='next', ctx=Load()),
                                                        args=[
                                                            GeneratorExp(
                                                                elt=Name(id='ps', ctx=Load()),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Name(id='ps', ctx=Store()),
                                                                        iter=Name(id='PAPER_SIZES', ctx=Load()),
                                                                        ifs=[
                                                                            Compare(
                                                                                left=Subscript(
                                                                                    value=Name(id='ps', ctx=Load()),
                                                                                    slice=Constant(value='key', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[
                                                                                    Attribute(
                                                                                        value=Name(id='record', ctx=Load()),
                                                                                        attr='format',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        is_async=0,
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='width', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='paper_size', ctx=Load()),
                                                        slice=Constant(value='width', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='height', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='paper_size', ctx=Load()),
                                                        slice=Constant(value='height', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='orientation',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='Landscape', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='width', ctx=Store()),
                                                        Name(id='height', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    Name(id='height', ctx=Load()),
                                                    Name(id='width', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='print_page_width',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='width', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='print_page_height',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='height', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
