Module(
    body=[
        ImportFrom(
            lineno=2,
            col_offset=0,
            end_lineno=2,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=5,
            col_offset=0,
            end_lineno=8,
            end_col_offset=56,
            name='L10nCoDocumentType',
            bases=[
                Attribute(
                    lineno=5,
                    col_offset=25,
                    end_lineno=5,
                    end_col_offset=37,
                    value=Name(lineno=5, col_offset=25, end_lineno=5, end_col_offset=31, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=6,
                    col_offset=4,
                    end_lineno=6,
                    end_col_offset=47,
                    targets=[Name(lineno=6, col_offset=4, end_lineno=6, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=6, col_offset=15, end_lineno=6, end_col_offset=47, value='l10n_latam.identification.type', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=56,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=25, id='l10n_co_document_code', ctx=Store())],
                    value=Call(
                        lineno=8,
                        col_offset=28,
                        end_lineno=8,
                        end_col_offset=56,
                        func=Attribute(
                            lineno=8,
                            col_offset=28,
                            end_lineno=8,
                            end_col_offset=39,
                            value=Name(lineno=8, col_offset=28, end_lineno=8, end_col_offset=34, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=8, col_offset=40, end_lineno=8, end_col_offset=55, value='Document Code', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)