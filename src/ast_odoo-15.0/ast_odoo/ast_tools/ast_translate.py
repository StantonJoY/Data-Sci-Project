Module(
    body=[
        Import(
            names=[alias(name='codecs', asname=None)],
        ),
        Import(
            names=[alias(name='fnmatch', asname=None)],
        ),
        Import(
            names=[alias(name='functools', asname=None)],
        ),
        Import(
            names=[alias(name='inspect', asname=None)],
        ),
        Import(
            names=[alias(name='io', asname=None)],
        ),
        Import(
            names=[alias(name='locale', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='polib', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='tarfile', asname=None)],
        ),
        Import(
            names=[alias(name='tempfile', asname=None)],
        ),
        Import(
            names=[alias(name='threading', asname=None)],
        ),
        ImportFrom(
            module='collections',
            names=[
                alias(name='defaultdict', asname=None),
                alias(name='namedtuple', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='datetime',
            names=[alias(name='datetime', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='os.path',
            names=[alias(name='join', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='pathlib',
            names=[alias(name='Path', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='babel.messages',
            names=[alias(name='extract', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='lxml',
            names=[
                alias(name='etree', asname=None),
                alias(name='html', asname=None),
            ],
            level=0,
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            module=None,
            names=[
                alias(name='config', asname=None),
                alias(name='pycompat', asname=None),
            ],
            level=1,
        ),
        ImportFrom(
            module='misc',
            names=[
                alias(name='file_open', asname=None),
                alias(name='get_iso_codes', asname=None),
                alias(name='SKIPPED_ELEMENT_TYPES', asname=None),
            ],
            level=1,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='WEB_TRANSLATION_COMMENT', ctx=Store())],
            value=Constant(value='openerp-web', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='SKIPPED_ELEMENTS', ctx=Store())],
            value=Tuple(
                elts=[
                    Constant(value='script', kind=None),
                    Constant(value='style', kind=None),
                    Constant(value='title', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_LOCALE2WIN32', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='af_ZA', kind=None),
                    Constant(value='sq_AL', kind=None),
                    Constant(value='ar_SA', kind=None),
                    Constant(value='eu_ES', kind=None),
                    Constant(value='be_BY', kind=None),
                    Constant(value='bs_BA', kind=None),
                    Constant(value='bg_BG', kind=None),
                    Constant(value='ca_ES', kind=None),
                    Constant(value='hr_HR', kind=None),
                    Constant(value='zh_CN', kind=None),
                    Constant(value='zh_TW', kind=None),
                    Constant(value='cs_CZ', kind=None),
                    Constant(value='da_DK', kind=None),
                    Constant(value='nl_NL', kind=None),
                    Constant(value='et_EE', kind=None),
                    Constant(value='fa_IR', kind=None),
                    Constant(value='ph_PH', kind=None),
                    Constant(value='fi_FI', kind=None),
                    Constant(value='fr_FR', kind=None),
                    Constant(value='fr_BE', kind=None),
                    Constant(value='fr_CH', kind=None),
                    Constant(value='fr_CA', kind=None),
                    Constant(value='ga', kind=None),
                    Constant(value='gl_ES', kind=None),
                    Constant(value='ka_GE', kind=None),
                    Constant(value='de_DE', kind=None),
                    Constant(value='el_GR', kind=None),
                    Constant(value='gu', kind=None),
                    Constant(value='he_IL', kind=None),
                    Constant(value='hi_IN', kind=None),
                    Constant(value='hu', kind=None),
                    Constant(value='is_IS', kind=None),
                    Constant(value='id_ID', kind=None),
                    Constant(value='it_IT', kind=None),
                    Constant(value='ja_JP', kind=None),
                    Constant(value='kn_IN', kind=None),
                    Constant(value='km_KH', kind=None),
                    Constant(value='ko_KR', kind=None),
                    Constant(value='lo_LA', kind=None),
                    Constant(value='lt_LT', kind=None),
                    Constant(value='lat', kind=None),
                    Constant(value='ml_IN', kind=None),
                    Constant(value='mi_NZ', kind=None),
                    Constant(value='mn', kind=None),
                    Constant(value='no_NO', kind=None),
                    Constant(value='nn_NO', kind=None),
                    Constant(value='pl', kind=None),
                    Constant(value='pt_PT', kind=None),
                    Constant(value='pt_BR', kind=None),
                    Constant(value='ro_RO', kind=None),
                    Constant(value='ru_RU', kind=None),
                    Constant(value='sr_CS', kind=None),
                    Constant(value='sk_SK', kind=None),
                    Constant(value='sl_SI', kind=None),
                    Constant(value='es_AR', kind=None),
                    Constant(value='es_BO', kind=None),
                    Constant(value='es_CL', kind=None),
                    Constant(value='es_CO', kind=None),
                    Constant(value='es_CR', kind=None),
                    Constant(value='es_DO', kind=None),
                    Constant(value='es_EC', kind=None),
                    Constant(value='es_ES', kind=None),
                    Constant(value='es_GT', kind=None),
                    Constant(value='es_HN', kind=None),
                    Constant(value='es_MX', kind=None),
                    Constant(value='es_NI', kind=None),
                    Constant(value='es_PA', kind=None),
                    Constant(value='es_PE', kind=None),
                    Constant(value='es_PR', kind=None),
                    Constant(value='es_PY', kind=None),
                    Constant(value='es_SV', kind=None),
                    Constant(value='es_UY', kind=None),
                    Constant(value='es_VE', kind=None),
                    Constant(value='sv_SE', kind=None),
                    Constant(value='ta_IN', kind=None),
                    Constant(value='th_TH', kind=None),
                    Constant(value='tr_TR', kind=None),
                    Constant(value='uk_UA', kind=None),
                    Constant(value='vi_VN', kind=None),
                    Constant(value='tlh_TLH', kind=None),
                ],
                values=[
                    Constant(value='Afrikaans_South Africa', kind=None),
                    Constant(value='Albanian_Albania', kind=None),
                    Constant(value='Arabic_Saudi Arabia', kind=None),
                    Constant(value='Basque_Spain', kind=None),
                    Constant(value='Belarusian_Belarus', kind=None),
                    Constant(value='Bosnian_Bosnia and Herzegovina', kind=None),
                    Constant(value='Bulgarian_Bulgaria', kind=None),
                    Constant(value='Catalan_Spain', kind=None),
                    Constant(value='Croatian_Croatia', kind=None),
                    Constant(value='Chinese_China', kind=None),
                    Constant(value='Chinese_Taiwan', kind=None),
                    Constant(value='Czech_Czech Republic', kind=None),
                    Constant(value='Danish_Denmark', kind=None),
                    Constant(value='Dutch_Netherlands', kind=None),
                    Constant(value='Estonian_Estonia', kind=None),
                    Constant(value='Farsi_Iran', kind=None),
                    Constant(value='Filipino_Philippines', kind=None),
                    Constant(value='Finnish_Finland', kind=None),
                    Constant(value='French_France', kind=None),
                    Constant(value='French_France', kind=None),
                    Constant(value='French_France', kind=None),
                    Constant(value='French_France', kind=None),
                    Constant(value='Scottish Gaelic', kind=None),
                    Constant(value='Galician_Spain', kind=None),
                    Constant(value='Georgian_Georgia', kind=None),
                    Constant(value='German_Germany', kind=None),
                    Constant(value='Greek_Greece', kind=None),
                    Constant(value='Gujarati_India', kind=None),
                    Constant(value='Hebrew_Israel', kind=None),
                    Constant(value='Hindi', kind=None),
                    Constant(value='Hungarian_Hungary', kind=None),
                    Constant(value='Icelandic_Iceland', kind=None),
                    Constant(value='Indonesian_Indonesia', kind=None),
                    Constant(value='Italian_Italy', kind=None),
                    Constant(value='Japanese_Japan', kind=None),
                    Constant(value='Kannada', kind=None),
                    Constant(value='Khmer', kind=None),
                    Constant(value='Korean_Korea', kind=None),
                    Constant(value='Lao_Laos', kind=None),
                    Constant(value='Lithuanian_Lithuania', kind=None),
                    Constant(value='Latvian_Latvia', kind=None),
                    Constant(value='Malayalam_India', kind=None),
                    Constant(value='Maori', kind=None),
                    Constant(value='Cyrillic_Mongolian', kind=None),
                    Constant(value='Norwegian_Norway', kind=None),
                    Constant(value='Norwegian-Nynorsk_Norway', kind=None),
                    Constant(value='Polish_Poland', kind=None),
                    Constant(value='Portuguese_Portugal', kind=None),
                    Constant(value='Portuguese_Brazil', kind=None),
                    Constant(value='Romanian_Romania', kind=None),
                    Constant(value='Russian_Russia', kind=None),
                    Constant(value='Serbian (Cyrillic)_Serbia and Montenegro', kind=None),
                    Constant(value='Slovak_Slovakia', kind=None),
                    Constant(value='Slovenian_Slovenia', kind=None),
                    Constant(value='Spanish_Spain', kind=None),
                    Constant(value='Spanish_Spain', kind=None),
                    Constant(value='Spanish_Spain', kind=None),
                    Constant(value='Spanish_Spain', kind=None),
                    Constant(value='Spanish_Spain', kind=None),
                    Constant(value='Spanish_Spain', kind=None),
                    Constant(value='Spanish_Spain', kind=None),
                    Constant(value='Spanish_Spain', kind=None),
                    Constant(value='Spanish_Spain', kind=None),
                    Constant(value='Spanish_Spain', kind=None),
                    Constant(value='Spanish_Spain', kind=None),
                    Constant(value='Spanish_Spain', kind=None),
                    Constant(value='Spanish_Spain', kind=None),
                    Constant(value='Spanish_Spain', kind=None),
                    Constant(value='Spanish_Spain', kind=None),
                    Constant(value='Spanish_Spain', kind=None),
                    Constant(value='Spanish_Spain', kind=None),
                    Constant(value='Spanish_Spain', kind=None),
                    Constant(value='Spanish_Spain', kind=None),
                    Constant(value='Swedish_Sweden', kind=None),
                    Constant(value='English_Australia', kind=None),
                    Constant(value='Thai_Thailand', kind=None),
                    Constant(value='Turkish_Turkey', kind=None),
                    Constant(value='Ukrainian_Ukraine', kind=None),
                    Constant(value='Vietnamese_Viet Nam', kind=None),
                    Constant(value='Klingon', kind=None),
                ],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='ENGLISH_SMALL_WORDS', ctx=Store())],
            value=Call(
                func=Name(id='set', ctx=Load()),
                args=[
                    Call(
                        func=Attribute(
                            value=Constant(value='as at by do go if in me no of ok on or to up us we', kind=None),
                            attr='split',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Import(
            names=[alias(name='csv', asname=None)],
        ),
        ClassDef(
            name='UNIX_LINE_TERMINATOR',
            bases=[
                Attribute(
                    value=Name(id='csv', ctx=Load()),
                    attr='excel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='lineterminator', ctx=Store())],
                    value=Constant(value='\n', kind=None),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        Expr(
            value=Call(
                func=Attribute(
                    value=Name(id='csv', ctx=Load()),
                    attr='register_dialect',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='UNIX', kind=None),
                    Name(id='UNIX_LINE_TERMINATOR', ctx=Load()),
                ],
                keywords=[],
            ),
        ),
        FunctionDef(
            name='encode',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='s', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assert(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='s', ctx=Load()),
                            Name(id='str', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    msg=None,
                ),
                Return(
                    value=Name(id='s', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='TRANSLATED_ELEMENTS', ctx=Store())],
            value=Set(
                elts=[
                    Constant(value='abbr', kind=None),
                    Constant(value='b', kind=None),
                    Constant(value='bdi', kind=None),
                    Constant(value='bdo', kind=None),
                    Constant(value='br', kind=None),
                    Constant(value='cite', kind=None),
                    Constant(value='code', kind=None),
                    Constant(value='data', kind=None),
                    Constant(value='del', kind=None),
                    Constant(value='dfn', kind=None),
                    Constant(value='em', kind=None),
                    Constant(value='font', kind=None),
                    Constant(value='i', kind=None),
                    Constant(value='ins', kind=None),
                    Constant(value='kbd', kind=None),
                    Constant(value='keygen', kind=None),
                    Constant(value='mark', kind=None),
                    Constant(value='math', kind=None),
                    Constant(value='meter', kind=None),
                    Constant(value='output', kind=None),
                    Constant(value='progress', kind=None),
                    Constant(value='q', kind=None),
                    Constant(value='ruby', kind=None),
                    Constant(value='s', kind=None),
                    Constant(value='samp', kind=None),
                    Constant(value='small', kind=None),
                    Constant(value='span', kind=None),
                    Constant(value='strong', kind=None),
                    Constant(value='sub', kind=None),
                    Constant(value='sup', kind=None),
                    Constant(value='time', kind=None),
                    Constant(value='u', kind=None),
                    Constant(value='var', kind=None),
                    Constant(value='wbr', kind=None),
                    Constant(value='text', kind=None),
                ],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='TRANSLATED_ATTRS', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='dict', ctx=Load()),
                    attr='fromkeys',
                    ctx=Load(),
                ),
                args=[
                    Set(
                        elts=[
                            Constant(value='string', kind=None),
                            Constant(value='add-label', kind=None),
                            Constant(value='help', kind=None),
                            Constant(value='sum', kind=None),
                            Constant(value='avg', kind=None),
                            Constant(value='confirm', kind=None),
                            Constant(value='placeholder', kind=None),
                            Constant(value='alt', kind=None),
                            Constant(value='title', kind=None),
                            Constant(value='aria-label', kind=None),
                            Constant(value='aria-keyshortcuts', kind=None),
                            Constant(value='aria-placeholder', kind=None),
                            Constant(value='aria-roledescription', kind=None),
                            Constant(value='aria-valuetext', kind=None),
                            Constant(value='value_label', kind=None),
                            Constant(value='data-tooltip', kind=None),
                        ],
                    ),
                    Lambda(
                        args=arguments(
                            posonlyargs=[],
                            args=[arg(arg='e', annotation=None, type_comment=None)],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=Constant(value=True, kind=None),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='translate_attrib_value',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='node', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='classes', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='node', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='class', kind=None),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                            attr='split',
                            ctx=Load(),
                        ),
                        args=[Constant(value=' ', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=BoolOp(
                        op=Or(),
                        values=[
                            BoolOp(
                                op=And(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='node', ctx=Load()),
                                                    attr='tag',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='input', kind=None)],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='node', ctx=Load()),
                                                            attr='attrib',
                                                            ctx=Load(),
                                                        ),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='type', kind=None),
                                                        Constant(value='text', kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='text', kind=None)],
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Constant(value='datetimepicker-input', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='classes', ctx=Load())],
                                    ),
                                ],
                            ),
                            BoolOp(
                                op=And(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='node', ctx=Load()),
                                                    attr='tag',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='input', kind=None)],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='node', ctx=Load()),
                                                            attr='attrib',
                                                            ctx=Load(),
                                                        ),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='type', kind=None)],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='hidden', kind=None)],
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Constant(value='o_translatable_input_hidden', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='classes', ctx=Load())],
                                    ),
                                ],
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Expr(
            value=Call(
                func=Attribute(
                    value=Name(id='TRANSLATED_ATTRS', ctx=Load()),
                    attr='update',
                    ctx=Load(),
                ),
                args=[],
                keywords=[
                    keyword(
                        arg='value',
                        value=Name(id='translate_attrib_value', ctx=Load()),
                    ),
                    keyword(
                        arg='text',
                        value=Lambda(
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='e', annotation=None, type_comment=None)],
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
                                            value=Name(id='e', ctx=Load()),
                                            attr='tag',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='field', kind=None)],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='e', ctx=Load()),
                                                    attr='attrib',
                                                    ctx=Load(),
                                                ),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='widget', kind=None),
                                                Constant(value='', kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='url', kind=None)],
                                    ),
                                ],
                            ),
                        ),
                    ),
                    keyword(
                        arg=None,
                        value=DictComp(
                            key=JoinedStr(
                                values=[
                                    Constant(value='t-attf-', kind=None),
                                    FormattedValue(
                                        value=Name(id='attr', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                ],
                            ),
                            value=Name(id='cond', ctx=Load()),
                            generators=[
                                comprehension(
                                    target=Tuple(
                                        elts=[
                                            Name(id='attr', ctx=Store()),
                                            Name(id='cond', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='TRANSLATED_ATTRS', ctx=Load()),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    ifs=[],
                                    is_async=0,
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        ),
        Assign(
            targets=[Name(id='avoid_pattern', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='\\s*<!DOCTYPE', kind=None),
                    BinOp(
                        left=BinOp(
                            left=Attribute(
                                value=Name(id='re', ctx=Load()),
                                attr='IGNORECASE',
                                ctx=Load(),
                            ),
                            op=BitOr(),
                            right=Attribute(
                                value=Name(id='re', ctx=Load()),
                                attr='MULTILINE',
                                ctx=Load(),
                            ),
                        ),
                        op=BitOr(),
                        right=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='UNICODE',
                            ctx=Load(),
                        ),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='node_pattern', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='<[^>]*>(.*)</[^<]*>', kind=None),
                    BinOp(
                        left=BinOp(
                            left=Attribute(
                                value=Name(id='re', ctx=Load()),
                                attr='DOTALL',
                                ctx=Load(),
                            ),
                            op=BitOr(),
                            right=Attribute(
                                value=Name(id='re', ctx=Load()),
                                attr='MULTILINE',
                                ctx=Load(),
                            ),
                        ),
                        op=BitOr(),
                        right=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='UNICODE',
                            ctx=Load(),
                        ),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='translate_xml_node',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='node', annotation=None, type_comment=None),
                    arg(arg='callback', annotation=None, type_comment=None),
                    arg(arg='parse', annotation=None, type_comment=None),
                    arg(arg='serialize', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return the translation of the given XML/HTML node.\n\n        :param callback: callback(text) returns translated text or None\n        :param parse: parse(text) returns a node (text is unicode)\n        :param serialize: serialize(node) returns unicode text\n    ', kind=None),
                ),
                FunctionDef(
                    name='nonspace',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='text', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return whether ``text`` is a string with non-space characters. ', kind=None),
                        ),
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[Name(id='text', ctx=Load())],
                                        keywords=[],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='text', ctx=Load()),
                                                attr='isspace',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='translatable',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='node', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return whether the given node can be translated as a whole. ', kind=None),
                        ),
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='node', ctx=Load()),
                                            attr='tag',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[Name(id='TRANSLATED_ELEMENTS', ctx=Load())],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='any', ctx=Load()),
                                            args=[
                                                GeneratorExp(
                                                    elt=Call(
                                                        func=Attribute(
                                                            value=Name(id='key', ctx=Load()),
                                                            attr='startswith',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='t-', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='key', ctx=Store()),
                                                            iter=Attribute(
                                                                value=Name(id='node', ctx=Load()),
                                                                attr='attrib',
                                                                ctx=Load(),
                                                            ),
                                                            ifs=[],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    Call(
                                        func=Name(id='all', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Call(
                                                    func=Name(id='translatable', ctx=Load()),
                                                    args=[Name(id='child', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='child', ctx=Store()),
                                                        iter=Name(id='node', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='hastext',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='node', annotation=None, type_comment=None),
                            arg(arg='pos', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=0, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return whether the given node contains some text to translate at the\n            given child node position.  The text may be before the child node,\n            inside it, or after it.\n        ', kind=None),
                        ),
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Name(id='nonspace', ctx=Load()),
                                        args=[
                                            IfExp(
                                                test=Name(id='pos', ctx=Load()),
                                                body=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='node', ctx=Load()),
                                                        slice=BinOp(
                                                            left=Name(id='pos', ctx=Load()),
                                                            op=Sub(),
                                                            right=Constant(value=1, kind=None),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr='tail',
                                                    ctx=Load(),
                                                ),
                                                orelse=Attribute(
                                                    value=Name(id='node', ctx=Load()),
                                                    attr='text',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='pos', ctx=Load()),
                                                ops=[Lt()],
                                                comparators=[
                                                    Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[Name(id='node', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='translatable', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='node', ctx=Load()),
                                                        slice=Name(id='pos', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Call(
                                                        func=Name(id='any', ctx=Load()),
                                                        args=[
                                                            GeneratorExp(
                                                                elt=BoolOp(
                                                                    op=And(),
                                                                    values=[
                                                                        Name(id='val', ctx=Load()),
                                                                        Compare(
                                                                            left=Name(id='key', ctx=Load()),
                                                                            ops=[In()],
                                                                            comparators=[Name(id='TRANSLATED_ATTRS', ctx=Load())],
                                                                        ),
                                                                        Call(
                                                                            func=Subscript(
                                                                                value=Name(id='TRANSLATED_ATTRS', ctx=Load()),
                                                                                slice=Name(id='key', ctx=Load()),
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Subscript(
                                                                                    value=Name(id='node', ctx=Load()),
                                                                                    slice=Name(id='pos', ctx=Load()),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ],
                                                                ),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Tuple(
                                                                            elts=[
                                                                                Name(id='key', ctx=Store()),
                                                                                Name(id='val', ctx=Store()),
                                                                            ],
                                                                            ctx=Store(),
                                                                        ),
                                                                        iter=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Name(id='node', ctx=Load()),
                                                                                        slice=Name(id='pos', ctx=Load()),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='attrib',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='items',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                        ifs=[],
                                                                        is_async=0,
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='hastext', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='node', ctx=Load()),
                                                                slice=Name(id='pos', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='hastext', ctx=Load()),
                                                        args=[
                                                            Name(id='node', ctx=Load()),
                                                            BinOp(
                                                                left=Name(id='pos', ctx=Load()),
                                                                op=Add(),
                                                                right=Constant(value=1, kind=None),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='process',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='node', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Translate the given node. ', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='node', ctx=Load()),
                                            Name(id='SKIPPED_ELEMENT_TYPES', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='node', ctx=Load()),
                                            attr='tag',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[Name(id='SKIPPED_ELEMENTS', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='node', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='t-translation', kind=None),
                                                        Constant(value='', kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='strip',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='off', kind=None)],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='node', ctx=Load()),
                                                    attr='tag',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='attribute', kind=None)],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='node', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='name', kind=None)],
                                                    keywords=[],
                                                ),
                                                ops=[NotIn()],
                                                comparators=[Name(id='TRANSLATED_ATTRS', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='node', ctx=Load()),
                                                        attr='getparent',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ops=[Is()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='avoid_pattern', ctx=Load()),
                                                    attr='match',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='node', ctx=Load()),
                                                                attr='text',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='pos', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        While(
                            test=Constant(value=True, kind=None),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='hastext', ctx=Load()),
                                        args=[
                                            Name(id='node', ctx=Load()),
                                            Name(id='pos', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='div', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='etree', ctx=Load()),
                                                    attr='Element',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='div', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='div', ctx=Load()),
                                                    attr='text',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    IfExp(
                                                        test=Name(id='pos', ctx=Load()),
                                                        body=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='node', ctx=Load()),
                                                                slice=BinOp(
                                                                    left=Name(id='pos', ctx=Load()),
                                                                    op=Sub(),
                                                                    right=Constant(value=1, kind=None),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            attr='tail',
                                                            ctx=Load(),
                                                        ),
                                                        orelse=Attribute(
                                                            value=Name(id='node', ctx=Load()),
                                                            attr='text',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        While(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='pos', ctx=Load()),
                                                        ops=[Lt()],
                                                        comparators=[
                                                            Call(
                                                                func=Name(id='len', ctx=Load()),
                                                                args=[Name(id='node', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    Call(
                                                        func=Name(id='translatable', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='node', ctx=Load()),
                                                                slice=Name(id='pos', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='div', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='node', ctx=Load()),
                                                                slice=Name(id='pos', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='content', ctx=Store())],
                                            value=Subscript(
                                                value=Call(
                                                    func=Name(id='serialize', ctx=Load()),
                                                    args=[Name(id='div', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                slice=Slice(
                                                    lower=Constant(value=5, kind=None),
                                                    upper=UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=6, kind=None),
                                                    ),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='original', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='content', ctx=Load()),
                                                    attr='strip',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='translated', ctx=Store())],
                                            value=Call(
                                                func=Name(id='callback', ctx=Load()),
                                                args=[Name(id='original', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='translated', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='result', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='content', ctx=Load()),
                                                            attr='replace',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='original', ctx=Load()),
                                                            Name(id='translated', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='div', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='parse_html', ctx=Load()),
                                                        args=[
                                                            JoinedStr(
                                                                values=[
                                                                    Constant(value='<div>', kind=None),
                                                                    FormattedValue(
                                                                        value=Name(id='result', ctx=Load()),
                                                                        conversion=-1,
                                                                        format_spec=None,
                                                                    ),
                                                                    Constant(value='</div>', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='pos', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Subscript(
                                                                        value=Name(id='node', ctx=Load()),
                                                                        slice=BinOp(
                                                                            left=Name(id='pos', ctx=Load()),
                                                                            op=Sub(),
                                                                            right=Constant(value=1, kind=None),
                                                                        ),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='tail',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Attribute(
                                                                value=Name(id='div', ctx=Load()),
                                                                attr='text',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='node', ctx=Load()),
                                                                    attr='text',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Attribute(
                                                                value=Name(id='div', ctx=Load()),
                                                                attr='text',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        While(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='div', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Gt()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='node', ctx=Load()),
                                                            attr='insert',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='pos', ctx=Load()),
                                                            Subscript(
                                                                value=Name(id='div', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                AugAssign(
                                                    target=Name(id='pos', ctx=Store()),
                                                    op=Add(),
                                                    value=Constant(value=1, kind=None),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='pos', ctx=Load()),
                                        ops=[GtE()],
                                        comparators=[
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='node', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[Break()],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='process', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='node', ctx=Load()),
                                                slice=Name(id='pos', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                AugAssign(
                                    target=Name(id='pos', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='key', ctx=Store()),
                                    Name(id='val', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='node', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='val', ctx=Load()),
                                            Compare(
                                                left=Name(id='key', ctx=Load()),
                                                ops=[In()],
                                                comparators=[Name(id='TRANSLATED_ATTRS', ctx=Load())],
                                            ),
                                            Call(
                                                func=Subscript(
                                                    value=Name(id='TRANSLATED_ATTRS', ctx=Load()),
                                                    slice=Name(id='key', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='node', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='node', ctx=Load()),
                                                    attr='set',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='key', ctx=Load()),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Call(
                                                                func=Name(id='callback', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='val', ctx=Load()),
                                                                            attr='strip',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Name(id='val', ctx=Load()),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
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
                Expr(
                    value=Call(
                        func=Name(id='process', ctx=Load()),
                        args=[Name(id='node', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Name(id='node', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='parse_xml',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='text', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='etree', ctx=Load()),
                            attr='fromstring',
                            ctx=Load(),
                        ),
                        args=[Name(id='text', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='serialize_xml',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='node', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='etree', ctx=Load()),
                            attr='tostring',
                            ctx=Load(),
                        ),
                        args=[Name(id='node', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='method',
                                value=Constant(value='xml', kind=None),
                            ),
                            keyword(
                                arg='encoding',
                                value=Constant(value='unicode', kind=None),
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_HTML_PARSER', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='etree', ctx=Load()),
                    attr='HTMLParser',
                    ctx=Load(),
                ),
                args=[],
                keywords=[
                    keyword(
                        arg='encoding',
                        value=Constant(value='utf8', kind=None),
                    ),
                ],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='parse_html',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='text', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='html', ctx=Load()),
                            attr='fragment_fromstring',
                            ctx=Load(),
                        ),
                        args=[Name(id='text', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='parser',
                                value=Name(id='_HTML_PARSER', ctx=Load()),
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='serialize_html',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='node', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='etree', ctx=Load()),
                            attr='tostring',
                            ctx=Load(),
                        ),
                        args=[Name(id='node', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='method',
                                value=Constant(value='html', kind=None),
                            ),
                            keyword(
                                arg='encoding',
                                value=Constant(value='unicode', kind=None),
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='xml_translate',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='callback', annotation=None, type_comment=None),
                    arg(arg='value', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Translate an XML value (string), using `callback` for translating text\n        appearing in `value`.\n    ', kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='value', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Name(id='value', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Try(
                    body=[
                        Assign(
                            targets=[Name(id='root', ctx=Store())],
                            value=Call(
                                func=Name(id='parse_xml', ctx=Load()),
                                args=[Name(id='value', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='translate_xml_node', ctx=Load()),
                                args=[
                                    Name(id='root', ctx=Load()),
                                    Name(id='callback', ctx=Load()),
                                    Name(id='parse_xml', ctx=Load()),
                                    Name(id='serialize_xml', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='serialize_xml', ctx=Load()),
                                args=[Name(id='result', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Attribute(
                                value=Name(id='etree', ctx=Load()),
                                attr='ParseError',
                                ctx=Load(),
                            ),
                            name=None,
                            body=[
                                Assign(
                                    targets=[Name(id='root', ctx=Store())],
                                    value=Call(
                                        func=Name(id='parse_html', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='<div>%s</div>', kind='u'),
                                                op=Mod(),
                                                right=Name(id='value', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Call(
                                        func=Name(id='translate_xml_node', ctx=Load()),
                                        args=[
                                            Name(id='root', ctx=Load()),
                                            Name(id='callback', ctx=Load()),
                                            Name(id='parse_xml', ctx=Load()),
                                            Name(id='serialize_xml', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Subscript(
                                        value=Call(
                                            func=Name(id='serialize_xml', ctx=Load()),
                                            args=[Name(id='result', ctx=Load())],
                                            keywords=[],
                                        ),
                                        slice=Slice(
                                            lower=Constant(value=5, kind=None),
                                            upper=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=6, kind=None),
                                            ),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='html_translate',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='callback', annotation=None, type_comment=None),
                    arg(arg='value', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Translate an HTML value (string), using `callback` for translating text\n        appearing in `value`.\n    ', kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='value', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Name(id='value', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Try(
                    body=[
                        Assign(
                            targets=[Name(id='root', ctx=Store())],
                            value=Call(
                                func=Name(id='parse_html', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='<div>%s</div>', kind=None),
                                        op=Mod(),
                                        right=Name(id='value', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='translate_xml_node', ctx=Load()),
                                args=[
                                    Name(id='root', ctx=Load()),
                                    Name(id='callback', ctx=Load()),
                                    Name(id='parse_html', ctx=Load()),
                                    Name(id='serialize_html', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='value', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Name(id='serialize_html', ctx=Load()),
                                    args=[Name(id='result', ctx=Load())],
                                    keywords=[],
                                ),
                                slice=Slice(
                                    lower=Constant(value=5, kind=None),
                                    upper=UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=6, kind=None),
                                    ),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='ValueError', ctx=Load()),
                            name=None,
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='exception',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='Cannot translate malformed HTML, using source value instead', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
                Return(
                    value=Name(id='value', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='translate',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='name', annotation=None, type_comment=None),
                    arg(arg='source_type', annotation=None, type_comment=None),
                    arg(arg='lang', annotation=None, type_comment=None),
                    arg(arg='source', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Name(id='source', ctx=Load()),
                            Name(id='name', ctx=Load()),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='select value from ir_translation where lang=%s and type=%s and name=%s and src=%s and md5(src)=md5(%s)', kind=None),
                                    Tuple(
                                        elts=[
                                            Name(id='lang', ctx=Load()),
                                            Name(id='source_type', ctx=Load()),
                                            Call(
                                                func=Name(id='str', ctx=Load()),
                                                args=[Name(id='name', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Name(id='source', ctx=Load()),
                                            Name(id='source', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[
                        If(
                            test=Name(id='name', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='select value from ir_translation where lang=%s and type=%s and name=%s', kind=None),
                                            Tuple(
                                                elts=[
                                                    Name(id='lang', ctx=Load()),
                                                    Name(id='source_type', ctx=Load()),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='name', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Name(id='source', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='cr', ctx=Load()),
                                                    attr='execute',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='select value from ir_translation where lang=%s and type=%s and src=%s and md5(src)=md5(%s)', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Name(id='lang', ctx=Load()),
                                                            Name(id='source_type', ctx=Load()),
                                                            Name(id='source', ctx=Load()),
                                                            Name(id='source', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                    ],
                ),
                Assign(
                    targets=[Name(id='res_trans', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='cr', ctx=Load()),
                            attr='fetchone',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='res', ctx=Store())],
                    value=BoolOp(
                        op=Or(),
                        values=[
                            BoolOp(
                                op=And(),
                                values=[
                                    Name(id='res_trans', ctx=Load()),
                                    Subscript(
                                        value=Name(id='res_trans', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Name(id='res', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='translate_sql_constraint',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='key', annotation=None, type_comment=None),
                    arg(arg='lang', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='cr', ctx=Load()),
                            attr='execute',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value="\n        SELECT COALESCE(t.value, c.message) as message\n        FROM ir_model_constraint c\n        LEFT JOIN\n        (SELECT res_id, value FROM ir_translation\n         WHERE type='model'\n           AND name='ir.model.constraint,message'\n           AND lang=%s\n           AND value!='') AS t\n        ON c.id=t.res_id\n        WHERE name=%s and type='u'\n        ", kind=None),
                            Tuple(
                                elts=[
                                    Name(id='lang', ctx=Load()),
                                    Name(id='key', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Subscript(
                        value=Call(
                            func=Attribute(
                                value=Name(id='cr', ctx=Load()),
                                attr='fetchone',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                        slice=Constant(value=0, kind=None),
                        ctx=Load(),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='GettextAlias',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='_get_db',
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
                        Assign(
                            targets=[Name(id='db_name', ctx=Store())],
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='threading', ctx=Load()),
                                            attr='currentThread',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Constant(value='dbname', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='db_name', ctx=Load()),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='sql_db',
                                                ctx=Load(),
                                            ),
                                            attr='db_connect',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='db_name', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_cr',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='frame', annotation=None, type_comment=None),
                            arg(arg='allow_create', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Constant(value='cr', kind=None),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='frame', ctx=Load()),
                                        attr='f_locals',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='frame', ctx=Load()),
                                                    attr='f_locals',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='cr', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='cursor', kind=None),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='frame', ctx=Load()),
                                        attr='f_locals',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='frame', ctx=Load()),
                                                    attr='f_locals',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='cursor', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='s', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='frame', ctx=Load()),
                                        attr='f_locals',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='self', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='hasattr', ctx=Load()),
                                args=[
                                    Name(id='s', ctx=Load()),
                                    Constant(value='env', kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='s', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id='hasattr', ctx=Load()),
                                args=[
                                    Name(id='s', ctx=Load()),
                                    Constant(value='cr', kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='s', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                ImportFrom(
                                    module='odoo.http',
                                    names=[alias(name='request', asname=None)],
                                    level=0,
                                ),
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='RuntimeError', ctx=Load()),
                                    name=None,
                                    body=[Pass()],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        If(
                            test=Name(id='allow_create', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='db', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_db',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='db', ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Tuple(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='db', ctx=Load()),
                                                            attr='cursor',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Constant(value=None, kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_uid',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='frame', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Constant(value='uid', kind=None),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='frame', ctx=Load()),
                                        attr='f_locals',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='frame', ctx=Load()),
                                            attr='f_locals',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='uid', kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='user', kind=None),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='frame', ctx=Load()),
                                        attr='f_locals',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='frame', ctx=Load()),
                                                    attr='f_locals',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='user', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='s', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='frame', ctx=Load()),
                                        attr='f_locals',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='self', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='s', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='uid',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_lang',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='frame', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='lang', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='frame', ctx=Load()),
                                        attr='f_locals',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='context', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='lang', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='frame', ctx=Load()),
                                                    attr='f_locals',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='context', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='lang', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='lang', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='kwargs', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='frame', ctx=Load()),
                                                attr='f_locals',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='kwargs', kind=None),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='kwargs', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='context', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='lang', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='kwargs', ctx=Load()),
                                                        slice=Constant(value='context', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='lang', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='lang', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='s', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='frame', ctx=Load()),
                                                attr='f_locals',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='self', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='hasattr', ctx=Load()),
                                        args=[
                                            Name(id='s', ctx=Load()),
                                            Constant(value='env', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='lang', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='s', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='lang',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='lang', ctx=Load()),
                                    ),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Name(id='hasattr', ctx=Load()),
                                                args=[
                                                    Name(id='s', ctx=Load()),
                                                    Constant(value='localcontext', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='lang', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='s', ctx=Load()),
                                                                attr='localcontext',
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='lang', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='lang', ctx=Load()),
                                    ),
                                    body=[
                                        Try(
                                            body=[
                                                ImportFrom(
                                                    module='odoo.http',
                                                    names=[alias(name='request', asname=None)],
                                                    level=0,
                                                ),
                                                Assign(
                                                    targets=[Name(id='lang', ctx=Store())],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='lang',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='RuntimeError', ctx=Load()),
                                                    name=None,
                                                    body=[Pass()],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='lang', ctx=Load()),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='cr', ctx=Store()),
                                                        Name(id='dummy', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_cr',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='frame', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='allow_create',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='uid', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_uid',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='frame', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='cr', ctx=Load()),
                                                    Name(id='uid', ctx=Load()),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='env', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='odoo', ctx=Load()),
                                                                attr='api',
                                                                ctx=Load(),
                                                            ),
                                                            attr='Environment',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='cr', ctx=Load()),
                                                            Name(id='uid', ctx=Load()),
                                                            Dict(keys=[], values=[]),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='lang', ctx=Store())],
                                                    value=Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='env', ctx=Load()),
                                                                    slice=Constant(value='res.users', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='context_get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        slice=Constant(value='lang', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='lang', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__call__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='source', annotation=None, type_comment=None),
                        ],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='translation', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_translation',
                                    ctx=Load(),
                                ),
                                args=[Name(id='source', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assert(
                            test=UnaryOp(
                                op=Not(),
                                operand=BoolOp(
                                    op=And(),
                                    values=[
                                        Name(id='args', ctx=Load()),
                                        Name(id='kwargs', ctx=Load()),
                                    ],
                                ),
                            ),
                            msg=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='args', ctx=Load()),
                                    Name(id='kwargs', ctx=Load()),
                                ],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Return(
                                            value=BinOp(
                                                left=Name(id='translation', ctx=Load()),
                                                op=Mod(),
                                                right=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Name(id='args', ctx=Load()),
                                                        Name(id='kwargs', ctx=Load()),
                                                    ],
                                                ),
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Tuple(
                                                elts=[
                                                    Name(id='TypeError', ctx=Load()),
                                                    Name(id='ValueError', ctx=Load()),
                                                    Name(id='KeyError', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            name=None,
                                            body=[
                                                Assign(
                                                    targets=[Name(id='bad', ctx=Store())],
                                                    value=Name(id='translation', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='translation', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='source', ctx=Load()),
                                                        op=Mod(),
                                                        right=BoolOp(
                                                            op=Or(),
                                                            values=[
                                                                Name(id='args', ctx=Load()),
                                                                Name(id='kwargs', ctx=Load()),
                                                            ],
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='exception',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Bad translation %r for string %r', kind=None),
                                                            Name(id='bad', ctx=Load()),
                                                            Name(id='source', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='translation', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_translation',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='source', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Name(id='source', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cr', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='is_new_cr', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='frame', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='inspect', ctx=Load()),
                                            attr='currentframe',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='frame', ctx=Load()),
                                        ops=[Is()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Name(id='source', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='frame', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='frame', ctx=Load()),
                                        attr='f_back',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='frame', ctx=Load()),
                                    ),
                                    body=[
                                        Return(
                                            value=Name(id='source', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='frame', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='frame', ctx=Load()),
                                        attr='f_back',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='frame', ctx=Load()),
                                    ),
                                    body=[
                                        Return(
                                            value=Name(id='source', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='lang', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_lang',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='frame', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='lang', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='cr', ctx=Store()),
                                                        Name(id='is_new_cr', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_cr',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='frame', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='cr', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='env', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='odoo', ctx=Load()),
                                                                attr='api',
                                                                ctx=Load(),
                                                            ),
                                                            attr='Environment',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='cr', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='odoo', ctx=Load()),
                                                                attr='SUPERUSER_ID',
                                                                ctx=Load(),
                                                            ),
                                                            Dict(keys=[], values=[]),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='res', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='env', ctx=Load()),
                                                                slice=Constant(value='ir.translation', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='_get_source',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value=None, kind=None),
                                                            Tuple(
                                                                elts=[Constant(value='code', kind=None)],
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='lang', ctx=Load()),
                                                            Name(id='source', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='debug',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='no context cursor detected, skipping translation for "%r"', kind=None),
                                                            Name(id='source', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='debug',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='no translation language detected, skipping translation for "%r" ', kind=None),
                                                    Name(id='source', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='debug',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='translation went wrong for "%r", skipped', kind=None),
                                                    Name(id='source', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='cr', ctx=Load()),
                                            Name(id='is_new_cr', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='cr', ctx=Load()),
                                                    attr='close',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='res', ctx=Load()),
                                    Constant(value='', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='_lt',
            bases=[],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Lazy code translation\n\n    Similar to GettextAlias but the translation lookup will be done only at\n    __str__ execution.\n\n    A code using translated global variables such as:\n\n    LABEL = _lt("User")\n\n    def _compute_label(self):\n        context = {\'lang\': self.partner_id.lang}\n        self.user_label = LABEL\n\n    works as expected (unlike the classic GettextAlias implementation).\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='__slots__', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='_source', kind=None),
                            Constant(value='_args', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='source', annotation=None, type_comment=None),
                        ],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_source',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='source', ctx=Load()),
                            type_comment=None,
                        ),
                        Assert(
                            test=UnaryOp(
                                op=Not(),
                                operand=BoolOp(
                                    op=And(),
                                    values=[
                                        Name(id='args', ctx=Load()),
                                        Name(id='kwargs', ctx=Load()),
                                    ],
                                ),
                            ),
                            msg=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_args',
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='args', ctx=Load()),
                                    Name(id='kwargs', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__str__',
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
                        Assign(
                            targets=[Name(id='translation', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_', ctx=Load()),
                                    attr='_get_translation',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_source',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_args',
                                ctx=Load(),
                            ),
                            body=[
                                Try(
                                    body=[
                                        Return(
                                            value=BinOp(
                                                left=Name(id='translation', ctx=Load()),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_args',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Tuple(
                                                elts=[
                                                    Name(id='TypeError', ctx=Load()),
                                                    Name(id='ValueError', ctx=Load()),
                                                    Name(id='KeyError', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            name=None,
                                            body=[
                                                Assign(
                                                    targets=[Name(id='bad', ctx=Store())],
                                                    value=Name(id='translation', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='translation', ctx=Store())],
                                                    value=BinOp(
                                                        left=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_source',
                                                            ctx=Load(),
                                                        ),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_args',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='exception',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Bad translation %r for string %r', kind=None),
                                                            Name(id='bad', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_source',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='translation', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__eq__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='other', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Prevent using equal operators\n\n        Prevent direct comparisons with ``self``.\n        One should compare the translation of ``self._source`` as ``str(self) == X``.\n        ', kind=None),
                        ),
                        Raise(
                            exc=Call(
                                func=Name(id='NotImplementedError', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__lt__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='other', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='NotImplementedError', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__add__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='other', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='other', ctx=Load()),
                                    Name(id='str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='_', ctx=Load()),
                                                attr='_get_translation',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_source',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=Name(id='other', ctx=Load()),
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='other', ctx=Load()),
                                            Name(id='_lt', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Return(
                                            value=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='_', ctx=Load()),
                                                        attr='_get_translation',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_source',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Name(id='_', ctx=Load()),
                                                        attr='_get_translation',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='other', ctx=Load()),
                                                            attr='_source',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='NotImplemented', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__radd__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='other', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='other', ctx=Load()),
                                    Name(id='str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=BinOp(
                                        left=Name(id='other', ctx=Load()),
                                        op=Add(),
                                        right=Call(
                                            func=Attribute(
                                                value=Name(id='_', ctx=Load()),
                                                attr='_get_translation',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_source',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='NotImplemented', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Attribute(
                    value=Name(id='functools', ctx=Load()),
                    attr='total_ordering',
                    ctx=Load(),
                ),
            ],
        ),
        Assign(
            targets=[Name(id='_', ctx=Store())],
            value=Call(
                func=Name(id='GettextAlias', ctx=Load()),
                args=[],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='quote',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='s', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Returns quoted PO term string, with special PO characters escaped', kind=None),
                ),
                Assert(
                    test=Compare(
                        left=Constant(value='\\n', kind=None),
                        ops=[NotIn()],
                        comparators=[Name(id='s', ctx=Load())],
                    ),
                    msg=BinOp(
                        left=Constant(value="Translation terms may not include escaped newlines ('\\n'), please use only literal newlines! (in '%s')", kind=None),
                        op=Mod(),
                        right=Name(id='s', ctx=Load()),
                    ),
                ),
                Return(
                    value=BinOp(
                        left=Constant(value='"%s"', kind=None),
                        op=Mod(),
                        right=Call(
                            func=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='s', ctx=Load()),
                                                attr='replace',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='\\', kind=None),
                                                Constant(value='\\\\', kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='replace',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='"', kind=None),
                                        Constant(value='\\"', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                attr='replace',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='\n', kind=None),
                                Constant(value='\\n"\n"', kind=None),
                            ],
                            keywords=[],
                        ),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='re_escaped_char', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[Constant(value='(\\\\.)', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='re_escaped_replacements', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='n', kind=None),
                    Constant(value='t', kind=None),
                ],
                values=[
                    Constant(value='\n', kind=None),
                    Constant(value='\t', kind=None),
                ],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='_sub_replacement',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='match_obj', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='re_escaped_replacements', ctx=Load()),
                            attr='get',
                            ctx=Load(),
                        ),
                        args=[
                            Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='match_obj', ctx=Load()),
                                        attr='group',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value=1, kind=None)],
                                    keywords=[],
                                ),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
                            Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='match_obj', ctx=Load()),
                                        attr='group',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value=1, kind=None)],
                                    keywords=[],
                                ),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='unquote',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='str', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Returns unquoted PO term string, with special PO characters unescaped', kind=None),
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='re_escaped_char', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='_sub_replacement', ctx=Load()),
                            Subscript(
                                value=Name(id='str', ctx=Load()),
                                slice=Slice(
                                    lower=Constant(value=1, kind=None),
                                    upper=UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='TranslationFileReader',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='source', annotation=None, type_comment=None),
                    arg(arg='fileformat', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value='po', kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value=' Iterate over translation file to return Odoo translation entries ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Name(id='fileformat', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Constant(value='csv', kind=None)],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='CSVFileReader', ctx=Load()),
                                args=[Name(id='source', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Compare(
                        left=Name(id='fileformat', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Constant(value='po', kind=None)],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='PoFileReader', ctx=Load()),
                                args=[Name(id='source', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='_logger', ctx=Load()),
                            attr='info',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='Bad file format: %s', kind=None),
                            Name(id='fileformat', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Raise(
                    exc=Call(
                        func=Name(id='Exception', ctx=Load()),
                        args=[
                            Call(
                                func=Name(id='_', ctx=Load()),
                                args=[
                                    Constant(value='Bad file format: %s', kind=None),
                                    Name(id='fileformat', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                    cause=None,
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='CSVFileReader',
            bases=[],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='source', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='_reader', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='codecs', ctx=Load()),
                                    attr='getreader',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='utf-8', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='source',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='csv', ctx=Load()),
                                    attr='DictReader',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='_reader', ctx=Load()),
                                        args=[Name(id='source', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='quotechar',
                                        value=Constant(value='"', kind=None),
                                    ),
                                    keyword(
                                        arg='delimiter',
                                        value=Constant(value=',', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='prev_code_src',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__iter__',
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
                            target=Name(id='entry', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='source',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Subscript(
                                                value=Name(id='entry', ctx=Load()),
                                                slice=Constant(value='res_id', kind=None),
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='entry', ctx=Load()),
                                                        slice=Constant(value='res_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='isnumeric',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='entry', ctx=Load()),
                                                    slice=Constant(value='res_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='entry', ctx=Load()),
                                                        slice=Constant(value='res_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='entry', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='imd_name', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Subscript(
                                                                    value=Name(id='entry', ctx=Load()),
                                                                    slice=Constant(value='module', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                                Subscript(
                                                                    value=Name(id='entry', ctx=Load()),
                                                                    slice=Constant(value='imd_name', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='entry', ctx=Load()),
                                                                slice=Constant(value='res_id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='split',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='entry', ctx=Load()),
                                                            slice=Constant(value='res_id', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=None, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='entry', ctx=Load()),
                                                    slice=Constant(value='type', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='model', kind=None)],
                                            ),
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='entry', ctx=Load()),
                                                    slice=Constant(value='type', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='model_terms', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='entry', ctx=Load()),
                                                    slice=Constant(value='imd_model', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='entry', ctx=Load()),
                                                            slice=Constant(value='name', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='partition',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value=',', kind=None)],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='entry', ctx=Load()),
                                            slice=Constant(value='type', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='code', kind=None)],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='entry', ctx=Load()),
                                                    slice=Constant(value='src', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='prev_code_src',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='prev_code_src',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='entry', ctx=Load()),
                                                slice=Constant(value='src', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Yield(
                                        value=Name(id='entry', ctx=Load()),
                                    ),
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
        ClassDef(
            name='PoFileReader',
            bases=[],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Iterate over po file to return Odoo translation entries ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='source', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        FunctionDef(
                            name='get_pot_path',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='source_name', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='source_name', ctx=Load()),
                                                    Name(id='str', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='source_name', ctx=Load()),
                                                    attr='endswith',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='.po', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='path', ctx=Store())],
                                            value=Call(
                                                func=Name(id='Path', ctx=Load()),
                                                args=[Name(id='source_name', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='filename', ctx=Store())],
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='path', ctx=Load()),
                                                            attr='parent',
                                                            ctx=Load(),
                                                        ),
                                                        attr='parent',
                                                        ctx=Load(),
                                                    ),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Constant(value='.pot', kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='pot_path', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='path', ctx=Load()),
                                                    attr='with_name',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='filename', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='pot_path', ctx=Load()),
                                                                    attr='exists',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[Name(id='pot_path', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='source', ctx=Load()),
                                    Name(id='str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='pofile',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='polib', ctx=Load()),
                                            attr='pofile',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='source', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='pot_path', ctx=Store())],
                                    value=Call(
                                        func=Name(id='get_pot_path', ctx=Load()),
                                        args=[Name(id='source', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='pofile',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='polib', ctx=Load()),
                                            attr='pofile',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='source', ctx=Load()),
                                                            attr='read',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='decode',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='pot_path', ctx=Store())],
                                    value=Call(
                                        func=Name(id='get_pot_path', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='source', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=Name(id='pot_path', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='pofile',
                                                ctx=Load(),
                                            ),
                                            attr='merge',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='polib', ctx=Load()),
                                                    attr='pofile',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='pot_path', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__iter__',
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
                            target=Name(id='entry', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='pofile',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='entry', ctx=Load()),
                                        attr='obsolete',
                                        ctx=Load(),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='match', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='match',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='(module[s]?): (\\w+)', kind=None),
                                            Attribute(
                                                value=Name(id='entry', ctx=Load()),
                                                attr='comment',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='_', ctx=Store()),
                                                Name(id='module', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='match', ctx=Load()),
                                            attr='groups',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='comments', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value='\n', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            ListComp(
                                                elt=Name(id='c', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='c', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='entry', ctx=Load()),
                                                                    attr='comment',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='split',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='\n', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ifs=[
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='c', ctx=Load()),
                                                                        attr='startswith',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='module:', kind=None)],
                                                                    keywords=[],
                                                                ),
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
                                    targets=[Name(id='source', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='entry', ctx=Load()),
                                        attr='msgid',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='translation', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='entry', ctx=Load()),
                                        attr='msgstr',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='found_code_occurrence', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='occurrence', ctx=Store()),
                                            Name(id='line_number', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Attribute(
                                        value=Name(id='entry', ctx=Load()),
                                        attr='occurrences',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='match', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='re', ctx=Load()),
                                                    attr='match',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='(model|model_terms):([\\w.]+),([\\w]+):(\\w+)\\.([^ ]+)', kind=None),
                                                    Name(id='occurrence', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='match', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='type', ctx=Store()),
                                                                Name(id='model_name', ctx=Store()),
                                                                Name(id='field_name', ctx=Store()),
                                                                Name(id='module', ctx=Store()),
                                                                Name(id='xmlid', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='match', ctx=Load()),
                                                            attr='groups',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Yield(
                                                        value=Dict(
                                                            keys=[
                                                                Constant(value='type', kind=None),
                                                                Constant(value='imd_model', kind=None),
                                                                Constant(value='name', kind=None),
                                                                Constant(value='imd_name', kind=None),
                                                                Constant(value='res_id', kind=None),
                                                                Constant(value='src', kind=None),
                                                                Constant(value='value', kind=None),
                                                                Constant(value='comments', kind=None),
                                                                Constant(value='module', kind=None),
                                                            ],
                                                            values=[
                                                                Name(id='type', ctx=Load()),
                                                                Name(id='model_name', ctx=Load()),
                                                                BinOp(
                                                                    left=BinOp(
                                                                        left=Name(id='model_name', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Constant(value=',', kind=None),
                                                                    ),
                                                                    op=Add(),
                                                                    right=Name(id='field_name', ctx=Load()),
                                                                ),
                                                                Name(id='xmlid', ctx=Load()),
                                                                Constant(value=None, kind=None),
                                                                Name(id='source', ctx=Load()),
                                                                Name(id='translation', ctx=Load()),
                                                                Name(id='comments', ctx=Load()),
                                                                Name(id='module', ctx=Load()),
                                                            ],
                                                        ),
                                                    ),
                                                ),
                                                Continue(),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='match', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='re', ctx=Load()),
                                                    attr='match',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='(code):([\\w/.]+)', kind=None),
                                                    Name(id='occurrence', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='match', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='type', ctx=Store()),
                                                                Name(id='name', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='match', ctx=Load()),
                                                            attr='groups',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='found_code_occurrence', ctx=Load()),
                                                    body=[Continue()],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='found_code_occurrence', ctx=Store())],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Yield(
                                                        value=Dict(
                                                            keys=[
                                                                Constant(value='type', kind=None),
                                                                Constant(value='name', kind=None),
                                                                Constant(value='src', kind=None),
                                                                Constant(value='value', kind=None),
                                                                Constant(value='comments', kind=None),
                                                                Constant(value='res_id', kind=None),
                                                                Constant(value='module', kind=None),
                                                            ],
                                                            values=[
                                                                Name(id='type', ctx=Load()),
                                                                Name(id='name', ctx=Load()),
                                                                Name(id='source', ctx=Load()),
                                                                Name(id='translation', ctx=Load()),
                                                                Name(id='comments', ctx=Load()),
                                                                Call(
                                                                    func=Name(id='int', ctx=Load()),
                                                                    args=[Name(id='line_number', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                Name(id='module', ctx=Load()),
                                                            ],
                                                        ),
                                                    ),
                                                ),
                                                Continue(),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='match', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='re', ctx=Load()),
                                                    attr='match',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='(selection):([\\w.]+),([\\w]+)', kind=None),
                                                    Name(id='occurrence', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='match', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Skipped deprecated occurrence %s', kind=None),
                                                            Name(id='occurrence', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Continue(),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='match', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='re', ctx=Load()),
                                                    attr='match',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='(sql_constraint|constraint):([\\w.]+)', kind=None),
                                                    Name(id='occurrence', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='match', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Skipped deprecated occurrence %s', kind=None),
                                                            Name(id='occurrence', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Continue(),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='malformed po file: unknown occurrence: %s', kind=None),
                                                    Name(id='occurrence', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
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
        FunctionDef(
            name='TranslationFileWriter',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='target', annotation=None, type_comment=None),
                    arg(arg='fileformat', annotation=None, type_comment=None),
                    arg(arg='lang', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value='po', kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=' Iterate over translation file to return Odoo translation entries ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Name(id='fileformat', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Constant(value='csv', kind=None)],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='CSVFileWriter', ctx=Load()),
                                args=[Name(id='target', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Compare(
                        left=Name(id='fileformat', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Constant(value='po', kind=None)],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='PoFileWriter', ctx=Load()),
                                args=[Name(id='target', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='lang',
                                        value=Name(id='lang', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Compare(
                        left=Name(id='fileformat', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Constant(value='tgz', kind=None)],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='TarFileWriter', ctx=Load()),
                                args=[Name(id='target', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='lang',
                                        value=Name(id='lang', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Raise(
                    exc=Call(
                        func=Name(id='Exception', ctx=Load()),
                        args=[
                            BinOp(
                                left=Call(
                                    func=Name(id='_', ctx=Load()),
                                    args=[Constant(value='Unrecognized extension: must be one of .csv, .po, or .tgz (received .%s).', kind=None)],
                                    keywords=[],
                                ),
                                op=Mod(),
                                right=Name(id='fileformat', ctx=Load()),
                            ),
                        ],
                        keywords=[],
                    ),
                    cause=None,
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='CSVFileWriter',
            bases=[],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='target', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='writer',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pycompat', ctx=Load()),
                                    attr='csv_writer',
                                    ctx=Load(),
                                ),
                                args=[Name(id='target', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='dialect',
                                        value=Constant(value='UNIX', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='writer',
                                        ctx=Load(),
                                    ),
                                    attr='writerow',
                                    ctx=Load(),
                                ),
                                args=[
                                    Tuple(
                                        elts=[
                                            Constant(value='module', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='res_id', kind=None),
                                            Constant(value='src', kind=None),
                                            Constant(value='value', kind=None),
                                            Constant(value='comments', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write_rows',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='rows', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='module', ctx=Store()),
                                    Name(id='type', ctx=Store()),
                                    Name(id='name', ctx=Store()),
                                    Name(id='res_id', ctx=Store()),
                                    Name(id='src', ctx=Store()),
                                    Name(id='trad', ctx=Store()),
                                    Name(id='comments', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='rows', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='comments', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value='\n', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='comments', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='writer',
                                                ctx=Load(),
                                            ),
                                            attr='writerow',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Name(id='module', ctx=Load()),
                                                    Name(id='type', ctx=Load()),
                                                    Name(id='name', ctx=Load()),
                                                    Name(id='res_id', ctx=Load()),
                                                    Name(id='src', ctx=Load()),
                                                    Name(id='trad', ctx=Load()),
                                                    Name(id='comments', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
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
        ClassDef(
            name='PoFileWriter',
            bases=[],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Iterate over po file to return Odoo translation entries ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='target', annotation=None, type_comment=None),
                            arg(arg='lang', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='buffer',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='target', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='lang',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='lang', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='po',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='polib', ctx=Load()),
                                    attr='POFile',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write_rows',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='rows', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='grouped_rows', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='modules', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='module', ctx=Store()),
                                    Name(id='type', ctx=Store()),
                                    Name(id='name', ctx=Store()),
                                    Name(id='res_id', ctx=Store()),
                                    Name(id='src', ctx=Store()),
                                    Name(id='trad', ctx=Store()),
                                    Name(id='comments', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='rows', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='row', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='grouped_rows', ctx=Load()),
                                            attr='setdefault',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='src', ctx=Load()),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='row', ctx=Load()),
                                                    attr='setdefault',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='modules', kind=None),
                                                    Call(
                                                        func=Name(id='set', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='module', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='row', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='translation', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            Compare(
                                                left=Name(id='trad', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Name(id='src', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='row', ctx=Load()),
                                                    slice=Constant(value='translation', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='trad', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='row', ctx=Load()),
                                                    attr='setdefault',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='tnrs', kind=None),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Name(id='type', ctx=Load()),
                                                    Name(id='name', ctx=Load()),
                                                    Name(id='res_id', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='row', ctx=Load()),
                                                    attr='setdefault',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='comments', kind=None),
                                                    Call(
                                                        func=Name(id='set', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='comments', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='modules', ctx=Load()),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='module', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='src', ctx=Store()),
                                    Name(id='row', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='sorted', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='grouped_rows', ctx=Load()),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='lang',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='row', ctx=Load()),
                                                    slice=Constant(value='translation', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='row', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='translation', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='row', ctx=Load()),
                                                            slice=Constant(value='translation', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='add_entry',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='row', ctx=Load()),
                                                slice=Constant(value='modules', kind=None),
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='sorted', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='row', ctx=Load()),
                                                        slice=Constant(value='tnrs', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='src', ctx=Load()),
                                            Subscript(
                                                value=Name(id='row', ctx=Load()),
                                                slice=Constant(value='translation', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='row', ctx=Load()),
                                                slice=Constant(value='comments', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Import(
                            names=[alias(name='odoo.release', asname='release')],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='po',
                                        ctx=Load(),
                                    ),
                                    attr='header',
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=Constant(value='Translation of %s.\nThis file contains the translation of the following modules:\n%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='release', ctx=Load()),
                                            attr='description',
                                            ctx=Load(),
                                        ),
                                        Call(
                                            func=Attribute(
                                                value=Constant(value='', kind=None),
                                                attr='join',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                GeneratorExp(
                                                    elt=BinOp(
                                                        left=Constant(value='\t* %s\n', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='m', ctx=Load()),
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='m', ctx=Store()),
                                                            iter=Name(id='modules', ctx=Load()),
                                                            ifs=[],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='now', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='utcnow',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='strftime',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='%Y-%m-%d %H:%M+0000', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='po',
                                        ctx=Load(),
                                    ),
                                    attr='metadata',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='Project-Id-Version', kind=None),
                                    Constant(value='Report-Msgid-Bugs-To', kind=None),
                                    Constant(value='POT-Creation-Date', kind=None),
                                    Constant(value='PO-Revision-Date', kind=None),
                                    Constant(value='Last-Translator', kind=None),
                                    Constant(value='Language-Team', kind=None),
                                    Constant(value='MIME-Version', kind=None),
                                    Constant(value='Content-Type', kind=None),
                                    Constant(value='Content-Transfer-Encoding', kind=None),
                                    Constant(value='Plural-Forms', kind=None),
                                ],
                                values=[
                                    BinOp(
                                        left=Constant(value='%s %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='release', ctx=Load()),
                                                    attr='description',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='release', ctx=Load()),
                                                    attr='version',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value='', kind=None),
                                    Name(id='now', ctx=Load()),
                                    Name(id='now', ctx=Load()),
                                    Constant(value='', kind=None),
                                    Constant(value='', kind=None),
                                    Constant(value='1.0', kind=None),
                                    Constant(value='text/plain; charset=UTF-8', kind=None),
                                    Constant(value='', kind=None),
                                    Constant(value='', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='buffer',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='str', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='po',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='encode',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='add_entry',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='modules', annotation=None, type_comment=None),
                            arg(arg='tnrs', annotation=None, type_comment=None),
                            arg(arg='source', annotation=None, type_comment=None),
                            arg(arg='trad', annotation=None, type_comment=None),
                            arg(arg='comments', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='entry', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='polib', ctx=Load()),
                                    attr='POEntry',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='msgid',
                                        value=Name(id='source', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='msgstr',
                                        value=Name(id='trad', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='plural', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='modules', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Gt()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            Constant(value='s', kind=None),
                                        ],
                                    ),
                                    Constant(value='', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='entry', ctx=Load()),
                                    attr='comment',
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=Constant(value='module%s: %s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='plural', ctx=Load()),
                                        Call(
                                            func=Attribute(
                                                value=Constant(value=', ', kind=None),
                                                attr='join',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='modules', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='comments', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Attribute(
                                        value=Name(id='entry', ctx=Load()),
                                        attr='comment',
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=BinOp(
                                        left=Constant(value='\n', kind=None),
                                        op=Add(),
                                        right=Call(
                                            func=Attribute(
                                                value=Constant(value='\n', kind=None),
                                                attr='join',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='comments', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='code', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='typy', ctx=Store()),
                                    Name(id='name', ctx=Store()),
                                    Name(id='res_id', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='tnrs', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='typy', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='code', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='code', ctx=Store())],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='res_id', ctx=Store())],
                                            value=Constant(value=0, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='res_id', ctx=Load()),
                                                    Name(id='int', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='res_id', ctx=Load()),
                                                    attr='isdigit',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='entry', ctx=Load()),
                                                        attr='occurrences',
                                                        ctx=Load(),
                                                    ),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            BinOp(
                                                                left=Constant(value='%s:%s', kind='u'),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Name(id='typy', ctx=Load()),
                                                                        Name(id='name', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[Name(id='res_id', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='entry', ctx=Load()),
                                                        attr='occurrences',
                                                        ctx=Load(),
                                                    ),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            BinOp(
                                                                left=Constant(value='%s:%s:%s', kind='u'),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Name(id='typy', ctx=Load()),
                                                                        Name(id='name', ctx=Load()),
                                                                        Name(id='res_id', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            Constant(value='', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='code', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='entry', ctx=Load()),
                                                attr='flags',
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='python-format', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='po',
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='entry', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='TarFileWriter',
            bases=[],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='target', annotation=None, type_comment=None),
                            arg(arg='lang', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='tar',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tarfile', ctx=Load()),
                                    attr='open',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='fileobj',
                                        value=Name(id='target', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='mode',
                                        value=Constant(value='w|gz', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='lang',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='lang', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write_rows',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='rows', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='rows_by_module', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='row', ctx=Store()),
                            iter=Name(id='rows', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='module', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='row', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='rows_by_module', ctx=Load()),
                                                slice=Name(id='module', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='row', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='mod', ctx=Store()),
                                    Name(id='modrows', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='rows_by_module', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='io', ctx=Load()),
                                                    attr='BytesIO',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='buf', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[Name(id='po', ctx=Store())],
                                            value=Call(
                                                func=Name(id='PoFileWriter', ctx=Load()),
                                                args=[Name(id='buf', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='lang',
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='lang',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='po', ctx=Load()),
                                                    attr='write_rows',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='modrows', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='buf', ctx=Load()),
                                                    attr='seek',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=0, kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='info', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='tarfile', ctx=Load()),
                                                    attr='TarInfo',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='join', ctx=Load()),
                                                        args=[
                                                            Name(id='mod', ctx=Load()),
                                                            Constant(value='i18n', kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Constant(value='{basename}.{ext}', kind=None),
                                                                    attr='format',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='basename',
                                                                        value=BoolOp(
                                                                            op=Or(),
                                                                            values=[
                                                                                Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='lang',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                Name(id='mod', ctx=Load()),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='ext',
                                                                        value=IfExp(
                                                                            test=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='lang',
                                                                                ctx=Load(),
                                                                            ),
                                                                            body=Constant(value='po', kind=None),
                                                                            orelse=Constant(value='pot', kind=None),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='info', ctx=Load()),
                                                    attr='size',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='buf', ctx=Load()),
                                                            attr='getvalue',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tar',
                                                        ctx=Load(),
                                                    ),
                                                    attr='addfile',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='info', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='fileobj',
                                                        value=Name(id='buf', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tar',
                                        ctx=Load(),
                                    ),
                                    attr='close',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        FunctionDef(
            name='trans_export',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='lang', annotation=None, type_comment=None),
                    arg(arg='modules', annotation=None, type_comment=None),
                    arg(arg='buffer', annotation=None, type_comment=None),
                    arg(arg='format', annotation=None, type_comment=None),
                    arg(arg='cr', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='reader', ctx=Store())],
                    value=Call(
                        func=Name(id='TranslationModuleReader', ctx=Load()),
                        args=[Name(id='cr', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='modules',
                                value=Name(id='modules', ctx=Load()),
                            ),
                            keyword(
                                arg='lang',
                                value=Name(id='lang', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='writer', ctx=Store())],
                    value=Call(
                        func=Name(id='TranslationFileWriter', ctx=Load()),
                        args=[Name(id='buffer', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='fileformat',
                                value=Name(id='format', ctx=Load()),
                            ),
                            keyword(
                                arg='lang',
                                value=Name(id='lang', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='writer', ctx=Load()),
                            attr='write_rows',
                            ctx=Load(),
                        ),
                        args=[Name(id='reader', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='trans_parse_rml',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='de', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='res', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                For(
                    target=Name(id='n', ctx=Store()),
                    iter=Name(id='de', ctx=Load()),
                    body=[
                        For(
                            target=Name(id='m', ctx=Store()),
                            iter=Name(id='n', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='m', ctx=Load()),
                                                    Name(id='SKIPPED_ELEMENT_TYPES', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='m', ctx=Load()),
                                                    attr='text',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='string_list', ctx=Store())],
                                    value=ListComp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='s', ctx=Load()),
                                                        attr='replace',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='\n', kind=None),
                                                        Constant(value=' ', kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='strip',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='s', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='re', ctx=Load()),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='\\[\\[.+?\\]\\]', kind=None),
                                                        Attribute(
                                                            value=Name(id='m', ctx=Load()),
                                                            attr='text',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='s', ctx=Store()),
                                    iter=Name(id='string_list', ctx=Load()),
                                    body=[
                                        If(
                                            test=Name(id='s', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='res', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='s', ctx=Load()),
                                                                    attr='encode',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='utf8', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='res', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='trans_parse_rml', ctx=Load()),
                                        args=[Name(id='n', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Name(id='res', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_push',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='callback', annotation=None, type_comment=None),
                    arg(arg='term', annotation=None, type_comment=None),
                    arg(arg='source_line', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Sanity check before pushing translation terms ', kind=None),
                ),
                Assign(
                    targets=[Name(id='term', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='term', ctx=Load()),
                                    Constant(value='', kind=None),
                                ],
                            ),
                            attr='strip',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=Or(),
                        values=[
                            Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='term', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=8, kind=None)],
                            ),
                            Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='isalpha',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='x', ctx=Store()),
                                                iter=Name(id='term', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='callback', ctx=Load()),
                                args=[
                                    Name(id='term', ctx=Load()),
                                    Name(id='source_line', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='in_modules',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='object_name', annotation=None, type_comment=None),
                    arg(arg='modules', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                If(
                    test=Compare(
                        left=Constant(value='all', kind=None),
                        ops=[In()],
                        comparators=[Name(id='modules', ctx=Load())],
                    ),
                    body=[
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='module_dict', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='ir', kind=None),
                            Constant(value='res', kind=None),
                        ],
                        values=[
                            Constant(value='base', kind=None),
                            Constant(value='base', kind=None),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module', ctx=Store())],
                    value=Subscript(
                        value=Call(
                            func=Attribute(
                                value=Name(id='object_name', ctx=Load()),
                                attr='split',
                                ctx=Load(),
                            ),
                            args=[Constant(value='.', kind=None)],
                            keywords=[],
                        ),
                        slice=Constant(value=0, kind=None),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='module_dict', ctx=Load()),
                            attr='get',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='module', ctx=Load()),
                            Name(id='module', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Compare(
                        left=Name(id='module', ctx=Load()),
                        ops=[In()],
                        comparators=[Name(id='modules', ctx=Load())],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_extract_translatable_qweb_terms',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='element', annotation=None, type_comment=None),
                    arg(arg='callback', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Helper method to walk an etree document representing\n        a QWeb template, and call ``callback(term)`` for each\n        translatable term that is found in the document.\n\n        :param etree._Element element: root of etree document to extract terms from\n        :param Callable callback: a callable in the form ``f(term, source_line)``,\n                                  that will be called for each extracted term.\n    ', kind=None),
                ),
                For(
                    target=Name(id='el', ctx=Store()),
                    iter=Name(id='element', ctx=Load()),
                    body=[
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='el', ctx=Load()),
                                    Name(id='SKIPPED_ELEMENT_TYPES', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[Continue()],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='el', ctx=Load()),
                                                    attr='tag',
                                                    ctx=Load(),
                                                ),
                                                attr='lower',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[NotIn()],
                                        comparators=[Name(id='SKIPPED_ELEMENTS', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Constant(value='t-js', kind=None),
                                        ops=[NotIn()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='attrib',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=BoolOp(
                                            op=And(),
                                            values=[
                                                Compare(
                                                    left=Constant(value='t-jquery', kind=None),
                                                    ops=[In()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='el', ctx=Load()),
                                                            attr='attrib',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                Compare(
                                                    left=Constant(value='t-operation', kind=None),
                                                    ops=[NotIn()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='el', ctx=Load()),
                                                            attr='attrib',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='el', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='t-translation', kind=None),
                                                        Constant(value='', kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='strip',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='off', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='_push', ctx=Load()),
                                        args=[
                                            Name(id='callback', ctx=Load()),
                                            Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='text',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='sourceline',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='el', ctx=Load()),
                                                                attr='tag',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='isupper',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ),
                                            Compare(
                                                left=Constant(value='t-component', kind=None),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='el', ctx=Load()),
                                                        attr='attrib',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        For(
                                            target=Name(id='att', ctx=Store()),
                                            iter=Tuple(
                                                elts=[
                                                    Constant(value='title', kind=None),
                                                    Constant(value='alt', kind=None),
                                                    Constant(value='label', kind=None),
                                                    Constant(value='placeholder', kind=None),
                                                    Constant(value='aria-label', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='att', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='el', ctx=Load()),
                                                                attr='attrib',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Name(id='_push', ctx=Load()),
                                                                args=[
                                                                    Name(id='callback', ctx=Load()),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='el', ctx=Load()),
                                                                            attr='attrib',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Name(id='att', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='el', ctx=Load()),
                                                                        attr='sourceline',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='_extract_translatable_qweb_terms', ctx=Load()),
                                        args=[
                                            Name(id='el', ctx=Load()),
                                            Name(id='callback', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='_push', ctx=Load()),
                                args=[
                                    Name(id='callback', ctx=Load()),
                                    Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='tail',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='sourceline',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
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
        FunctionDef(
            name='babel_extract_qweb',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='fileobj', annotation=None, type_comment=None),
                    arg(arg='keywords', annotation=None, type_comment=None),
                    arg(arg='comment_tags', annotation=None, type_comment=None),
                    arg(arg='options', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Babel message extractor for qweb template files.\n\n    :param fileobj: the file-like object the messages should be extracted from\n    :param keywords: a list of keywords (i.e. function names) that should\n                     be recognized as translation functions\n    :param comment_tags: a list of translator tags to search for and\n                         include in the results\n    :param options: a dictionary of additional options (optional)\n    :return: an iterator over ``(lineno, funcname, message, comments)``\n             tuples\n    :rtype: Iterable\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='result', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                FunctionDef(
                    name='handle_text',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='text', annotation=None, type_comment=None),
                            arg(arg='lineno', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='result', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Tuple(
                                        elts=[
                                            Name(id='lineno', ctx=Load()),
                                            Constant(value=None, kind=None),
                                            Name(id='text', ctx=Load()),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='tree', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='etree', ctx=Load()),
                            attr='parse',
                            ctx=Load(),
                        ),
                        args=[Name(id='fileobj', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Name(id='_extract_translatable_qweb_terms', ctx=Load()),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='tree', ctx=Load()),
                                    attr='getroot',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            Name(id='handle_text', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Name(id='result', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='ImdInfo', ctx=Store())],
            value=Call(
                func=Name(id='namedtuple', ctx=Load()),
                args=[
                    Constant(value='ExternalId', kind=None),
                    List(
                        elts=[
                            Constant(value='name', kind=None),
                            Constant(value='model', kind=None),
                            Constant(value='res_id', kind=None),
                            Constant(value='module', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='TranslationModuleReader',
            bases=[],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=" Retrieve translated records per module\n\n    :param cr: cursor to database to export\n    :param modules: list of modules to filter the exported terms, can be ['all']\n                    records with no external id are always ignored\n    :param lang: language code to retrieve the translations\n                 retrieve source terms only if not set\n    ", kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='cr', annotation=None, type_comment=None),
                            arg(arg='modules', annotation=None, type_comment=None),
                            arg(arg='lang', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_cr',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='cr', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_modules',
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='modules', ctx=Load()),
                                    List(
                                        elts=[Constant(value='all', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_lang',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='lang', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='api',
                                        ctx=Load(),
                                    ),
                                    attr='Environment',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='cr', ctx=Load()),
                                    Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='SUPERUSER_ID',
                                        ctx=Load(),
                                    ),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_to_translate',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_path_list',
                                    ctx=Store(),
                                ),
                            ],
                            value=ListComp(
                                elt=Tuple(
                                    elts=[
                                        Name(id='path', ctx=Load()),
                                        Constant(value=True, kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='path', ctx=Store()),
                                        iter=Attribute(
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='addons',
                                                ctx=Load(),
                                            ),
                                            attr='__path__',
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_installed_modules',
                                    ctx=Store(),
                                ),
                            ],
                            value=ListComp(
                                elt=Subscript(
                                    value=Name(id='m', ctx=Load()),
                                    slice=Constant(value='name', kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='m', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='ir.module.module', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='search_read',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='state', kind=None),
                                                                Constant(value='=', kind=None),
                                                                Constant(value='installed', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='fields',
                                                    value=List(
                                                        elts=[Constant(value='name', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_export_translatable_records',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_export_translatable_resources',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__iter__',
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
                        Expr(
                            value=Constant(value=' Export ir.translation values for all retrieved records ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='IrTranslation', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.translation', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='module', ctx=Store()),
                                    Name(id='source', ctx=Store()),
                                    Name(id='name', ctx=Store()),
                                    Name(id='res_id', ctx=Store()),
                                    Name(id='ttype', ctx=Store()),
                                    Name(id='comments', ctx=Store()),
                                    Name(id='record_id', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_to_translate',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='trans', ctx=Store())],
                                    value=IfExp(
                                        test=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_lang',
                                            ctx=Load(),
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='IrTranslation', ctx=Load()),
                                                attr='_get_source',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                IfExp(
                                                    test=Compare(
                                                        left=Name(id='type', ctx=Load()),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value='code', kind=None)],
                                                    ),
                                                    body=Name(id='name', ctx=Load()),
                                                    orelse=Constant(value=None, kind=None),
                                                ),
                                                Name(id='ttype', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_lang',
                                                    ctx=Load(),
                                                ),
                                                Name(id='source', ctx=Load()),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='res_id',
                                                    value=Name(id='record_id', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                        orelse=Constant(value='', kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Yield(
                                        value=Tuple(
                                            elts=[
                                                Name(id='module', ctx=Load()),
                                                Name(id='ttype', ctx=Load()),
                                                Name(id='name', ctx=Load()),
                                                Name(id='res_id', ctx=Load()),
                                                Name(id='source', ctx=Load()),
                                                BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Call(
                                                            func=Name(id='encode', ctx=Load()),
                                                            args=[Name(id='trans', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        Constant(value='', kind=None),
                                                    ],
                                                ),
                                                Name(id='comments', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
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
                FunctionDef(
                    name='_push_translation',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='module', annotation=None, type_comment=None),
                            arg(arg='ttype', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='res_id', annotation=None, type_comment=None),
                            arg(arg='source', annotation=None, type_comment=None),
                            arg(arg='comments', annotation=None, type_comment=None),
                            arg(arg='record_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Insert a translation that will be used in the file generation\n        In po file will create an entry\n        #: <ttype>:<name>:<res_id>\n        #, <comment>\n        msgid "<source>"\n        record_id is the database id of the record being translated\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='sanitized_term', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='source', ctx=Load()),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    attr='strip',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sanitized_term', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='\\W+', kind=None),
                                    Constant(value='', kind=None),
                                    Name(id='sanitized_term', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='sanitized_term', ctx=Load()),
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='sanitized_term', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[LtE()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                ],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_to_translate',
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Tuple(
                                        elts=[
                                            Name(id='module', ctx=Load()),
                                            Name(id='source', ctx=Load()),
                                            Name(id='name', ctx=Load()),
                                            Name(id='res_id', ctx=Load()),
                                            Name(id='ttype', ctx=Load()),
                                            Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Name(id='comments', ctx=Load()),
                                                            Tuple(elts=[], ctx=Load()),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='record_id', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_translatable_records',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='imd_records', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Filter the records that are translatable\n\n        A record is considered as untranslatable if:\n        - it does not exist\n        - the model is flagged with _translate=False\n        - it is a field of a model flagged with _translate=False\n        - it is a selection of a field of a model flagged with _translate=False\n\n        :param records: a list of namedtuple ImdInfo belonging to the same model\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Name(id='next', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Name(id='iter', ctx=Load()),
                                            args=[Name(id='imd_records', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='model',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='model', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='error',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Unable to find object %r', kind=None),
                                            Name(id='model', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='_unknown', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='model', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    attr='_translate',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Name(id='model', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='res_ids', ctx=Store())],
                            value=ListComp(
                                elt=Attribute(
                                    value=Name(id='r', ctx=Load()),
                                    attr='res_id',
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='r', ctx=Store()),
                                        iter=Name(id='imd_records', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='records', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Name(id='model', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='res_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='exists',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='records', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Lt()],
                                comparators=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='res_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='missing_ids', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Name(id='set', ctx=Load()),
                                            args=[Name(id='res_ids', ctx=Load())],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Call(
                                            func=Name(id='set', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='records', ctx=Load()),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='missing_records', ctx=Store())],
                                    value=ListComp(
                                        elt=JoinedStr(
                                            values=[
                                                FormattedValue(
                                                    value=Attribute(
                                                        value=Name(id='r', ctx=Load()),
                                                        attr='module',
                                                        ctx=Load(),
                                                    ),
                                                    conversion=-1,
                                                    format_spec=None,
                                                ),
                                                Constant(value='.', kind=None),
                                                FormattedValue(
                                                    value=Attribute(
                                                        value=Name(id='r', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    conversion=-1,
                                                    format_spec=None,
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='r', ctx=Store()),
                                                iter=Name(id='imd_records', ctx=Load()),
                                                ifs=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='r', ctx=Load()),
                                                            attr='res_id',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[Name(id='missing_ids', ctx=Load())],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Unable to find records of type %r with external ids %s', kind=None),
                                            Name(id='model', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value=', ', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='missing_records', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='records', ctx=Load()),
                                    ),
                                    body=[
                                        Return(
                                            value=Name(id='records', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='model', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='ir.model.fields.selection', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='fields', ctx=Store())],
                                    value=Call(
                                        func=Name(id='defaultdict', ctx=Load()),
                                        args=[Name(id='list', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='selection', ctx=Store()),
                                    iter=Name(id='records', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='fields', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Name(id='selection', ctx=Load()),
                                                        attr='field_id',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='selection', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='field', ctx=Store()),
                                            Name(id='selection', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='fields', ctx=Load()),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='field_name', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='field', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='field_model', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='field', ctx=Load()),
                                                        attr='model',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='field_model', ctx=Load()),
                                                        ops=[Is()],
                                                        comparators=[Constant(value=None, kind=None)],
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='field_model', ctx=Load()),
                                                            attr='_translate',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Compare(
                                                        left=Name(id='field_name', ctx=Load()),
                                                        ops=[NotIn()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='field_model', ctx=Load()),
                                                                attr='_fields',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='records', ctx=Store()),
                                                    op=Sub(),
                                                    value=Name(id='selection', ctx=Load()),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='model', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='ir.model.fields', kind=None)],
                                    ),
                                    body=[
                                        For(
                                            target=Name(id='field', ctx=Store()),
                                            iter=Name(id='records', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='field_name', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='field', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='field_model', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='field', ctx=Load()),
                                                                attr='model',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='field_model', ctx=Load()),
                                                                ops=[Is()],
                                                                comparators=[Constant(value=None, kind=None)],
                                                            ),
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Attribute(
                                                                    value=Name(id='field_model', ctx=Load()),
                                                                    attr='_translate',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            Compare(
                                                                left=Name(id='field_name', ctx=Load()),
                                                                ops=[NotIn()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(id='field_model', ctx=Load()),
                                                                        attr='_fields',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='records', ctx=Store()),
                                                            op=Sub(),
                                                            value=Name(id='field', ctx=Load()),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='records', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_export_translatable_records',
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
                        Expr(
                            value=Constant(value=' Export translations of all translated records having an external id ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Constant(value='SELECT min(name), model, res_id, module\n                     FROM ir_model_data\n                    WHERE module = ANY(%s)\n                 GROUP BY model, res_id, module\n                 ORDER BY module, model, min(name)', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='all', kind=None),
                                ops=[NotIn()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_modules',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='query_param', ctx=Store())],
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_modules',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='query_param', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_installed_modules',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='query', ctx=Load()),
                                    Tuple(
                                        elts=[Name(id='query_param', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='records_per_model', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='dict', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='xml_name', ctx=Store()),
                                    Name(id='model', ctx=Store()),
                                    Name(id='res_id', ctx=Store()),
                                    Name(id='module', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='fetchall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='records_per_model', ctx=Load()),
                                                slice=Name(id='model', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Name(id='res_id', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='ImdInfo', ctx=Load()),
                                        args=[
                                            Name(id='xml_name', ctx=Load()),
                                            Name(id='model', ctx=Load()),
                                            Name(id='res_id', ctx=Load()),
                                            Name(id='module', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='model', ctx=Store()),
                                    Name(id='imd_per_id', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='records_per_model', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='records', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_translatable_records',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='imd_per_id', ctx=Load()),
                                                    attr='values',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='records', ctx=Load()),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                For(
                                    target=Name(id='record', ctx=Store()),
                                    iter=Name(id='records', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='module', ctx=Store())],
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Name(id='imd_per_id', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                attr='module',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='xml_name', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='%s.%s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='module', ctx=Load()),
                                                        Attribute(
                                                            value=Subscript(
                                                                value=Name(id='imd_per_id', ctx=Load()),
                                                                slice=Attribute(
                                                                    value=Name(id='record', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='field_name', ctx=Store()),
                                                    Name(id='field', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='_fields',
                                                        ctx=Load(),
                                                    ),
                                                    attr='items',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            body=[
                                                If(
                                                    test=Attribute(
                                                        value=Name(id='field', ctx=Load()),
                                                        attr='translate',
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='name', ctx=Store())],
                                                            value=BinOp(
                                                                left=BinOp(
                                                                    left=Name(id='model', ctx=Load()),
                                                                    op=Add(),
                                                                    right=Constant(value=',', kind=None),
                                                                ),
                                                                op=Add(),
                                                                right=Name(id='field_name', ctx=Load()),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Try(
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='value', ctx=Store())],
                                                                    value=BoolOp(
                                                                        op=Or(),
                                                                        values=[
                                                                            Subscript(
                                                                                value=Name(id='record', ctx=Load()),
                                                                                slice=Name(id='field_name', ctx=Load()),
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='', kind=None),
                                                                        ],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            handlers=[
                                                                ExceptHandler(
                                                                    type=Name(id='Exception', ctx=Load()),
                                                                    name=None,
                                                                    body=[Continue()],
                                                                ),
                                                            ],
                                                            orelse=[],
                                                            finalbody=[],
                                                        ),
                                                        For(
                                                            target=Name(id='term', ctx=Store()),
                                                            iter=Call(
                                                                func=Name(id='set', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='field', ctx=Load()),
                                                                            attr='get_trans_terms',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='value', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='trans_type', ctx=Store())],
                                                                    value=IfExp(
                                                                        test=Call(
                                                                            func=Name(id='callable', ctx=Load()),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(id='field', ctx=Load()),
                                                                                    attr='translate',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        body=Constant(value='model_terms', kind=None),
                                                                        orelse=Constant(value='model', kind=None),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_push_translation',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Name(id='module', ctx=Load()),
                                                                            Name(id='trans_type', ctx=Load()),
                                                                            Name(id='name', ctx=Load()),
                                                                            Name(id='xml_name', ctx=Load()),
                                                                            Name(id='term', ctx=Load()),
                                                                        ],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='record_id',
                                                                                value=Attribute(
                                                                                    value=Name(id='record', ctx=Load()),
                                                                                    attr='id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
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
                FunctionDef(
                    name='_get_module_from_path',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='mp', ctx=Store()),
                                    Name(id='rec', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_path_list',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='mp', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='mp', ctx=Load()),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='dirname', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='dirname',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='path', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='rec', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='path', ctx=Load()),
                                                    attr='startswith',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='mp', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Compare(
                                                left=Name(id='dirname', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Name(id='mp', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='path', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='path', ctx=Load()),
                                                slice=Slice(
                                                    lower=Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[Name(id='mp', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    upper=None,
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='path', ctx=Load()),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='os', ctx=Load()),
                                                                attr='path',
                                                                ctx=Load(),
                                                            ),
                                                            attr='sep',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Constant(value='base', kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_verified_module_filepaths',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fname', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                            arg(arg='root', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='fabsolutepath', ctx=Store())],
                            value=Call(
                                func=Name(id='join', ctx=Load()),
                                args=[
                                    Name(id='root', ctx=Load()),
                                    Name(id='fname', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='frelativepath', ctx=Store())],
                            value=Subscript(
                                value=Name(id='fabsolutepath', ctx=Load()),
                                slice=Slice(
                                    lower=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='path', ctx=Load())],
                                        keywords=[],
                                    ),
                                    upper=None,
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='display_path', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='addons%s', kind=None),
                                op=Mod(),
                                right=Name(id='frelativepath', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='module', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_module_from_path',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fabsolutepath', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Constant(value='all', kind=None),
                                                ops=[In()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_modules',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Name(id='module', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_modules',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Name(id='module', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_installed_modules',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='sep',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='/', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='display_path', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='display_path', ctx=Load()),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='path',
                                                            ctx=Load(),
                                                        ),
                                                        attr='sep',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='/', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Name(id='module', ctx=Load()),
                                            Name(id='fabsolutepath', ctx=Load()),
                                            Name(id='frelativepath', ctx=Load()),
                                            Name(id='display_path', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Constant(value=None, kind=None),
                                    Constant(value=None, kind=None),
                                    Constant(value=None, kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_babel_extract_terms',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fname', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                            arg(arg='root', annotation=None, type_comment=None),
                            arg(arg='extract_method', annotation=None, type_comment=None),
                            arg(arg='trans_type', annotation=None, type_comment=None),
                            arg(arg='extra_comments', annotation=None, type_comment=None),
                            arg(arg='extract_keywords', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value='python', kind=None),
                            Constant(value='code', kind=None),
                            Constant(value=None, kind=None),
                            Dict(
                                keys=[Constant(value='_', kind=None)],
                                values=[Constant(value=None, kind=None)],
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='module', ctx=Store()),
                                        Name(id='fabsolutepath', ctx=Store()),
                                        Name(id='_', ctx=Store()),
                                        Name(id='display_path', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_verified_module_filepaths',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='fname', ctx=Load()),
                                    Name(id='path', ctx=Load()),
                                    Name(id='root', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='module', ctx=Load()),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='extra_comments', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='extra_comments', ctx=Load()),
                                    List(elts=[], ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='src_file', ctx=Store())],
                            value=Call(
                                func=Name(id='open', ctx=Load()),
                                args=[
                                    Name(id='fabsolutepath', ctx=Load()),
                                    Constant(value='rb', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='options', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='extract_method', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='python', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='options', ctx=Load()),
                                            slice=Constant(value='encoding', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='UTF-8', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                For(
                                    target=Name(id='extracted', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='extract', ctx=Load()),
                                            attr='extract',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='extract_method', ctx=Load()),
                                            Name(id='src_file', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='keywords',
                                                value=Name(id='extract_keywords', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='options',
                                                value=Name(id='options', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='lineno', ctx=Store()),
                                                        Name(id='message', ctx=Store()),
                                                        Name(id='comments', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='extracted', ctx=Load()),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Constant(value=3, kind=None),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_push_translation',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='module', ctx=Load()),
                                                    Name(id='trans_type', ctx=Load()),
                                                    Name(id='display_path', ctx=Load()),
                                                    Name(id='lineno', ctx=Load()),
                                                    Call(
                                                        func=Name(id='encode', ctx=Load()),
                                                        args=[Name(id='message', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    BinOp(
                                                        left=Name(id='comments', ctx=Load()),
                                                        op=Add(),
                                                        right=Name(id='extra_comments', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='exception',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Failed to extract terms from %s', kind=None),
                                                    Name(id='fabsolutepath', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='src_file', ctx=Load()),
                                            attr='close',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_export_translatable_resources',
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
                        Expr(
                            value=Constant(value=' Export translations for static terms\n        \n        This will include:\n        - the python strings marked with _() or _lt()\n        - the javascript strings marked with _t() or _lt() inside static/src/js/\n        - the strings inside Qweb files inside static/src/xml/\n        ', kind=None),
                        ),
                        For(
                            target=Name(id='bin_path', ctx=Store()),
                            iter=List(
                                elts=[
                                    Constant(value='osv', kind=None),
                                    Constant(value='report', kind=None),
                                    Constant(value='modules', kind=None),
                                    Constant(value='service', kind=None),
                                    Constant(value='tools', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_path_list',
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='os', ctx=Load()),
                                                                attr='path',
                                                                ctx=Load(),
                                                            ),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='config', ctx=Load()),
                                                                slice=Constant(value='root_path', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='bin_path', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_path_list',
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Tuple(
                                        elts=[
                                            Subscript(
                                                value=Name(id='config', ctx=Load()),
                                                slice=Constant(value='root_path', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='debug',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Scanning modules at paths: %s', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_path_list',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='path', ctx=Store()),
                                    Name(id='recursive', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_path_list',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='debug',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Scanning files of modules at %s', kind=None),
                                            Name(id='path', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='root', ctx=Store()),
                                            Name(id='dummy', ctx=Store()),
                                            Name(id='files', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='walk',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='path', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='followlinks',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        For(
                                            target=Name(id='fname', ctx=Store()),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Name(id='fnmatch', ctx=Load()),
                                                    attr='filter',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='files', ctx=Load()),
                                                    Constant(value='*.py', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_babel_extract_terms',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='fname', ctx=Load()),
                                                            Name(id='path', ctx=Load()),
                                                            Name(id='root', ctx=Load()),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='extract_keywords',
                                                                value=Dict(
                                                                    keys=[
                                                                        Constant(value='_', kind=None),
                                                                        Constant(value='_lt', kind=None),
                                                                    ],
                                                                    values=[
                                                                        Constant(value=None, kind=None),
                                                                        Constant(value=None, kind=None),
                                                                    ],
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='fnmatch', ctx=Load()),
                                                    attr='fnmatch',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='root', ctx=Load()),
                                                    Constant(value='*/static/src*', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                For(
                                                    target=Name(id='fname', ctx=Store()),
                                                    iter=Call(
                                                        func=Attribute(
                                                            value=Name(id='fnmatch', ctx=Load()),
                                                            attr='filter',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='files', ctx=Load()),
                                                            Constant(value='*.js', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_babel_extract_terms',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='fname', ctx=Load()),
                                                                    Name(id='path', ctx=Load()),
                                                                    Name(id='root', ctx=Load()),
                                                                    Constant(value='javascript', kind=None),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='extra_comments',
                                                                        value=List(
                                                                            elts=[Name(id='WEB_TRANSLATION_COMMENT', ctx=Load())],
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='extract_keywords',
                                                                        value=Dict(
                                                                            keys=[
                                                                                Constant(value='_t', kind=None),
                                                                                Constant(value='_lt', kind=None),
                                                                            ],
                                                                            values=[
                                                                                Constant(value=None, kind=None),
                                                                                Constant(value=None, kind=None),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                                For(
                                                    target=Name(id='fname', ctx=Store()),
                                                    iter=Call(
                                                        func=Attribute(
                                                            value=Name(id='fnmatch', ctx=Load()),
                                                            attr='filter',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='files', ctx=Load()),
                                                            Constant(value='*.xml', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_babel_extract_terms',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='fname', ctx=Load()),
                                                                    Name(id='path', ctx=Load()),
                                                                    Name(id='root', ctx=Load()),
                                                                    Constant(value='odoo.tools.translate:babel_extract_qweb', kind=None),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='extra_comments',
                                                                        value=List(
                                                                            elts=[Name(id='WEB_TRANSLATION_COMMENT', ctx=Load())],
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='recursive', ctx=Load()),
                                            ),
                                            body=[Break()],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
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
        FunctionDef(
            name='trans_load',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='filename', annotation=None, type_comment=None),
                    arg(arg='lang', annotation=None, type_comment=None),
                    arg(arg='verbose', annotation=None, type_comment=None),
                    arg(arg='create_empty_translation', annotation=None, type_comment=None),
                    arg(arg='overwrite', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=True, kind=None),
                    Constant(value=False, kind=None),
                    Constant(value=False, kind=None),
                ],
            ),
            body=[
                Try(
                    body=[
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='file_open', ctx=Load()),
                                        args=[Name(id='filename', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='mode',
                                                value=Constant(value='rb', kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='fileobj', ctx=Store()),
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='loading %s', kind=None),
                                            Name(id='filename', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='fileformat', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='os', ctx=Load()),
                                                                attr='path',
                                                                ctx=Load(),
                                                            ),
                                                            attr='splitext',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='filename', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    slice=UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1, kind=None),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                slice=Slice(
                                                    lower=Constant(value=1, kind=None),
                                                    upper=None,
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='lower',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Name(id='trans_load_data', ctx=Load()),
                                        args=[
                                            Name(id='cr', ctx=Load()),
                                            Name(id='fileobj', ctx=Load()),
                                            Name(id='fileformat', ctx=Load()),
                                            Name(id='lang', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='verbose',
                                                value=Name(id='verbose', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='create_empty_translation',
                                                value=Name(id='create_empty_translation', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='overwrite',
                                                value=Name(id='overwrite', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='IOError', ctx=Load()),
                            name=None,
                            body=[
                                If(
                                    test=Name(id='verbose', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value="couldn't read translation file %s", kind=None),
                                                    Name(id='filename', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Constant(value=None, kind=None),
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='trans_load_data',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='fileobj', annotation=None, type_comment=None),
                    arg(arg='fileformat', annotation=None, type_comment=None),
                    arg(arg='lang', annotation=None, type_comment=None),
                    arg(arg='verbose', annotation=None, type_comment=None),
                    arg(arg='create_empty_translation', annotation=None, type_comment=None),
                    arg(arg='overwrite', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=True, kind=None),
                    Constant(value=False, kind=None),
                    Constant(value=False, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value="Populates the ir_translation table.\n\n    :param fileobj: buffer open to a translation file\n    :param fileformat: format of the `fielobj` file, one of 'po' or 'csv'\n    :param lang: language code of the translations contained in `fileobj`\n                 language must be present and activated in the database\n    :param verbose: increase log output\n    :param create_empty_translation: create an ir.translation record, even if no value\n                                     is provided in the translation entry\n    :param overwrite: if an ir.translation already exists for a term, replace it with\n                      the one in `fileobj`\n    ", kind=None),
                ),
                If(
                    test=Name(id='verbose', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='loading translation file for language %s', kind=None),
                                    Name(id='lang', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='env', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='api',
                                ctx=Load(),
                            ),
                            attr='Environment',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='cr', ctx=Load()),
                            Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='SUPERUSER_ID',
                                ctx=Load(),
                            ),
                            Dict(keys=[], values=[]),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Try(
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Name(id='env', ctx=Load()),
                                            slice=Constant(value='res.lang', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='_lang_get',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='lang', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='error',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value="Couldn't read translation for lang '%s', language not found", kind=None),
                                            Name(id='lang', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Constant(value=None, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='fileobj', ctx=Load()),
                                    attr='seek',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=0, kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='reader', ctx=Store())],
                            value=Call(
                                func=Name(id='TranslationFileReader', ctx=Load()),
                                args=[Name(id='fileobj', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fileformat',
                                        value=Name(id='fileformat', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Translation', ctx=Store())],
                            value=Subscript(
                                value=Name(id='env', ctx=Load()),
                                slice=Constant(value='ir.translation', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='irt_cursor', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Translation', ctx=Load()),
                                    attr='_get_import_cursor',
                                    ctx=Load(),
                                ),
                                args=[Name(id='overwrite', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='process_row',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='row', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value='Process a single PO (or POT) entry.', kind=None),
                                ),
                                Assign(
                                    targets=[Name(id='dic', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='dict', ctx=Load()),
                                            attr='fromkeys',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='type', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='src', kind=None),
                                                    Constant(value='value', kind=None),
                                                    Constant(value='comments', kind=None),
                                                    Constant(value='imd_model', kind=None),
                                                    Constant(value='imd_name', kind=None),
                                                    Constant(value='module', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='dic', ctx=Load()),
                                            slice=Constant(value='lang', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='lang', ctx=Load()),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='dic', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='row', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='create_empty_translation', ctx=Load()),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Subscript(
                                                    value=Name(id='dic', ctx=Load()),
                                                    slice=Constant(value='value', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[Return(value=None)],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='irt_cursor', ctx=Load()),
                                            attr='push',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='dic', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='row', ctx=Store()),
                            iter=Name(id='reader', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='process_row', ctx=Load()),
                                        args=[Name(id='row', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='irt_cursor', ctx=Load()),
                                    attr='finish',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Translation', ctx=Load()),
                                    attr='clear_caches',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='verbose', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='translation file loaded successfully', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='IOError', ctx=Load()),
                            name=None,
                            body=[
                                Assign(
                                    targets=[Name(id='iso_lang', ctx=Store())],
                                    value=Call(
                                        func=Name(id='get_iso_codes', ctx=Load()),
                                        args=[Name(id='lang', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='filename', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='[lang: %s][format: %s]', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Name(id='iso_lang', ctx=Load()),
                                                        Constant(value='new', kind=None),
                                                    ],
                                                ),
                                                Name(id='fileformat', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='exception',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value="couldn't read translation file %s", kind=None),
                                            Name(id='filename', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='get_locales',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='lang', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                If(
                    test=Compare(
                        left=Name(id='lang', ctx=Load()),
                        ops=[Is()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='lang', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='locale', ctx=Load()),
                                        attr='getdefaultlocale',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Compare(
                        left=Attribute(
                            value=Name(id='os', ctx=Load()),
                            attr='name',
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Constant(value='nt', kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='lang', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_LOCALE2WIN32', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='lang', ctx=Load()),
                                    Name(id='lang', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                FunctionDef(
                    name='process',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='enc', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='ln', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='locale', ctx=Load()),
                                    attr='_build_localename',
                                    ctx=Load(),
                                ),
                                args=[
                                    Tuple(
                                        elts=[
                                            Name(id='lang', ctx=Load()),
                                            Name(id='enc', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Yield(
                                value=Name(id='ln', ctx=Load()),
                            ),
                        ),
                        Assign(
                            targets=[Name(id='nln', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='locale', ctx=Load()),
                                    attr='normalize',
                                    ctx=Load(),
                                ),
                                args=[Name(id='ln', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='nln', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Name(id='ln', ctx=Load())],
                            ),
                            body=[
                                Expr(
                                    value=Yield(
                                        value=Name(id='nln', ctx=Load()),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                For(
                    target=Name(id='x', ctx=Store()),
                    iter=Call(
                        func=Name(id='process', ctx=Load()),
                        args=[Constant(value='utf8', kind=None)],
                        keywords=[],
                    ),
                    body=[
                        Expr(
                            value=Yield(
                                value=Name(id='x', ctx=Load()),
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='prefenc', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='locale', ctx=Load()),
                            attr='getpreferredencoding',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='prefenc', ctx=Load()),
                    body=[
                        For(
                            target=Name(id='x', ctx=Store()),
                            iter=Call(
                                func=Name(id='process', ctx=Load()),
                                args=[Name(id='prefenc', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Yield(
                                        value=Name(id='x', ctx=Load()),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='prefenc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Dict(
                                        keys=[
                                            Constant(value='latin1', kind=None),
                                            Constant(value='iso-8859-1', kind=None),
                                            Constant(value='cp1252', kind=None),
                                        ],
                                        values=[
                                            Constant(value='latin9', kind=None),
                                            Constant(value='iso8859-15', kind=None),
                                            Constant(value='1252', kind=None),
                                        ],
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='prefenc', ctx=Load()),
                                            attr='lower',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='prefenc', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='x', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='process', ctx=Load()),
                                        args=[Name(id='prefenc', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Yield(
                                                value=Name(id='x', ctx=Load()),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                ),
                Expr(
                    value=Yield(
                        value=Name(id='lang', ctx=Load()),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='resetlocale',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                For(
                    target=Name(id='ln', ctx=Store()),
                    iter=Call(
                        func=Name(id='get_locales', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    body=[
                        Try(
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='locale', ctx=Load()),
                                            attr='setlocale',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='locale', ctx=Load()),
                                                attr='LC_ALL',
                                                ctx=Load(),
                                            ),
                                            Name(id='ln', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='locale', ctx=Load()),
                                        attr='Error',
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[Continue()],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
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
        FunctionDef(
            name='load_language',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='lang', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=" Loads a translation terms for a language.\n    Used mainly to automate language loading at db initialization.\n\n    :param lang: language ISO code with optional _underscore_ and l10n flavor (ex: 'fr', 'fr_BE', but not 'fr-BE')\n    :type lang: str\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='env', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='api',
                                ctx=Load(),
                            ),
                            attr='Environment',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='cr', ctx=Load()),
                            Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='SUPERUSER_ID',
                                ctx=Load(),
                            ),
                            Dict(keys=[], values=[]),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='installer', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Subscript(
                                value=Name(id='env', ctx=Load()),
                                slice=Constant(value='base.language.install', kind=None),
                                ctx=Load(),
                            ),
                            attr='create',
                            ctx=Load(),
                        ),
                        args=[
                            Dict(
                                keys=[Constant(value='lang', kind=None)],
                                values=[Name(id='lang', ctx=Load())],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='installer', ctx=Load()),
                            attr='lang_install',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
