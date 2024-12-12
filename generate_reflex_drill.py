from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image,PageBreak
from reportlab.lib.pagesizes import A4
import math
import numpy as np



class reflex_report():
  
    def create_first_page(self,story, styles):
        # Custom styles for better presentation
        header_data = [[
            Image('hyperlab_logo.png', width=1.2*inch, height=0.5*inch),
            Paragraph(
                "<font color='#2E4053' size='16'><b>Hyperlab Sportech Pvt. Ltd. </b></font><br/>"
                "<font color='#5D6D7E' size='10'>Advanced Performance Assessment</font>",
                styles['Normal']
            )
        ]]
        header_table = Table(header_data, colWidths=[1.5*inch, 5.5*inch])
        header_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (1, 0), (1, 0), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
        ]))
        story.append(header_table)
        
        # Decorative Line
        line_table = Table([['']], colWidths=[7.5*inch], rowHeights=[2])
        line_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#2E4053')),
            ('LINEBELOW', (0, 0), (-1, -1), 2, colors.HexColor('#2E4053'))
        ]))
        story.append(line_table)
        
        story.append(Spacer(1, 20))
    
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=1,  # Center alignment
            textColor=colors.HexColor('#2E4053')
        )
        
        section_title_style = ParagraphStyle(
            'SectionTitle',
            parent=styles['Heading2'],
            fontSize=16,
            spaceBefore=20,
            spaceAfter=12,
            textColor=colors.HexColor('#2E4053')
        )
        
        intro_paragraph_style = ParagraphStyle(
            'IntroParagraph',
            parent=styles['Normal'],
            fontSize=11,
            leading=16,
            spaceBefore=6,
            spaceAfter=8,
            firstLineIndent=0,
            alignment=4  # Justified alignment
        )
        
        highlight_text_style = ParagraphStyle(
            'HighlightText',
            parent=styles['Normal'],
            fontSize=11,
            leading=16,
            textColor=colors.HexColor('#2E4053'),
            backColor=colors.HexColor('#F8F9F9'),
            borderPadding=5
        )

        # Title
        story.append(Paragraph("Reflex Drill Performance Report", title_style))
        
        # Information table
        current_date = datetime.now().strftime("%Y-%m-%d")
        info_data = [
            ["Student Name:", student_name, "Date of Assessment:", current_date],
            ["Device Used:", "HELIOS", "Drill Type:", "Reflex Response Drill"],
            ["Test Duration:", "Variable (20 points)", "Assessed by:", instructor_name]
        ]
        
        info_table = Table(info_data, colWidths=[1.5*inch, 2*inch, 1.5*inch, 2*inch])
        info_table.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E8E8E8')),
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#F4F6F7')),
            ('BACKGROUND', (2, 0), (2, -1), colors.HexColor('#F4F6F7')),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2E4053')),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('PADDING', (0, 0), (-1, -1), 8),
        ]))
        
        story.append(info_table)
        story.append(Spacer(1, 20))

        # Introduction Section
        story.append(Paragraph("Introduction", section_title_style))
        
        # Enhanced introduction paragraphs
        intro_text = "The <b>Reflex Drill</b> is designed to assess and enhance an athlete's <b>reflexes</b> and <b>neuromuscular response time</b>. Reflexes play a crucial role in many sports, where the ability to react swiftly to changing stimuli can significantly impact performance. This drill measures reaction times using <b>HELIOS technology</b>, which creates a precise and standardized testing environment."
        story.append(Paragraph(intro_text, intro_paragraph_style))
        
        story.append(Spacer(1, 1))
        
        intro_text2 = "The purpose of this drill is to help athletes understand their <b>reflex speed</b>, <b>motor response accuracy</b>, and potential differences between their left and right sides. By analyzing this data, athletes can identify areas where improvement is needed, optimizing their training for quicker reaction times and better overall agility. The comprehensive feedback provided serves as a valuable tool for refining reflexive abilities, crucial for peak athletic performance."
        story.append(Paragraph(intro_text2, intro_paragraph_style))
        
        story.append(Spacer(1, 2))

        story.append(Paragraph("Procedure", section_title_style))
        
        # Step-by-Step Procedure Box
        procedure_data = [
            ["Step", "Description", "Details"],
            ["1. Initialization", "System calibration\nSensor preparation", "HELIOS device startup\nMovement tracking enabled"],
            ["2. Drill Start", "Athlete readiness\nSystem activation", "Press and hold start button\nWait for system signal"],
            ["3. Target Movement", "Bilateral targets\nRandom intervals", "Left (-40°) and right (40°)\n500-2000ms intervals"],
            ["4. Response Detection", "LIDAR monitoring\nTiming measurement", "Successful tap recording\nTimeout monitoring"],
            ["5. Reset Position", "Return to center\nPreparation phase", "Home position return\nNext target preparation"],
            ["6. Completion", "20 total points\nPerformance analysis", "10 points per side\nReaction time analysis"]
        ]
        
        procedure_table = Table(procedure_data, colWidths=[1.5*inch, 2.5*inch, 2*inch])
        procedure_table.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E8E8E8')),
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2E4053')),
            ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#F4F6F7')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('PADDING', (0, 0), (-1, -1), 8),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
        
        story.append(procedure_table)
        
        return story

    def calculate_metrics(self,scores):
        # Filter successful reactions (non-zero values)
        def calculate_point_score(reaction_time):
            if not reaction_time or reaction_time <= 0:
                return 0  # Missed point or invalid time
            reaction_time = abs(reaction_time)  # Use absolute value of reaction time
            if reaction_time <= 300:
                return 0.5  # Full score for reactions under 300ms
            elif reaction_time <= 500:
                # Linear scale between 300ms (0.5 points) and 500ms (0.3 points)
                return 0.5 - (reaction_time - 300) * (0.2 / 200)
            else:
                return 0.3  # Minimum score for reactions over 500ms

        # Filter successful reactions (non-zero values)
        self.successful_reactions = [abs(score) for score in scores if score != 0]
        
        # Calculate total successful reactions
        self.total_successful_reactions = len(self.successful_reactions)

        # Calculate scores for each reaction
        reaction_scores = [calculate_point_score(rt) for rt in scores]
        total_score = sum(reaction_scores)
        self.final_score = min(10, total_score)  # Ensure score doesn't exceed 10
        
        # Calculate normalized percentage score (0-100 scale)
        self.final_score_percentage = (self.final_score / 10) * 100

        # Calculate average reaction time
        self.avg_reaction_time = sum(self.successful_reactions) / self.total_successful_reactions if self.total_successful_reactions > 0 else 0
        
        # Find fastest and slowest reactions
        self.slowest_reaction = max(self.successful_reactions) if self.successful_reactions else None
        self.fastest_reaction = min(self.successful_reactions) if self.successful_reactions else None

        # Calculate missed targets (zeros in the score)
        self.missed_targets = scores.count(0)

        # Additional parameters:
        # Number of left and right side reactions
        self.left_side_reactions = [abs(score) for score in scores if score < 0]
        self.right_side_reactions = [abs(score) for score in scores if score > 0]

        self.left_fastest_reaction = min(self.left_side_reactions) if self.left_side_reactions else 0
        self.left_slowest_reaction = max(self.left_side_reactions) if self.left_side_reactions else 0
        self.right_fastest_reaction = min(self.right_side_reactions) if self.right_side_reactions else 0
        self.right_slowest_reaction = max(self.right_side_reactions) if self.right_side_reactions else 0

        # Count of left and right side successful reactions
        self.left_side_count = len(self.left_side_reactions)
        self.right_side_count = len(self.right_side_reactions)
        
        # Average reaction time for left and right sides
        self.avg_left_reaction_time = sum(self.left_side_reactions) / self.left_side_count if self.left_side_count > 0 else 0
        self.avg_right_reaction_time = sum(self.right_side_reactions) / self.right_side_count if self.right_side_count > 0 else 0

        # Calculate scores for each side
        left_scores = [calculate_point_score(rt) for rt in self.left_side_reactions]
        right_scores = [calculate_point_score(rt) for rt in self.right_side_reactions]
        
        # Calculate side-specific scores
        self.left_score = sum(left_scores)
        self.right_score = sum(right_scores)
        
        # Calculate normalized percentage scores for sides
        max_side_score = 5  # Since total score is 10, each side has max 5 points
        self.left_score_percentage = (self.left_score / max_side_score) * 100
        self.right_score_percentage = (self.right_score / max_side_score) * 100

        # Calculate lateral balance score based on new scoring system
        total_side_score = self.left_score + self.right_score
        if total_side_score > 0:
            self.lbs = 100 - abs((self.left_score - self.right_score) / total_side_score * 100)
        else:
            self.lbs = 0

        # Calculate consistency scores based on point variations
        left_score_std = np.std(left_scores) if left_scores else 0
        right_score_std = np.std(right_scores) if right_scores else 0
        self.left_cs = 100 * (1 - left_score_std / 0.5) if left_scores else 0  # 0.5 is max possible score
        self.right_cs = 100 * (1 - right_score_std / 0.5) if right_scores else 0
        self.overall_cs = (self.left_cs + self.right_cs) / 2

        # Update RTS (Reaction Time Score) based on point scoring
        self.left_rts = self.left_score_percentage
        self.right_rts = self.right_score_percentage
        self.overall_rts = self.final_score_percentage
        
        # Update accuracy scores based on successful hits
        self.left_as = 100 * (self.left_side_count / 10)
        self.right_as = 100 * (self.right_side_count / 10)
        self.overall_as = 100 * (self.total_successful_reactions / 20)
        
        # SATS scores remain proportional to new scoring system
        self.left_sats = 0.5 * self.left_rts + 0.5 * self.left_as
        self.right_sats = 0.5 * self.right_rts + 0.5 * self.right_as
        self.overall_sats = (self.left_sats + self.right_sats) / 2        # 6. Missed Tap Penalty (MTP)
        self.mtp = 5 * self.missed_targets
        self.optimal_reaction_time=500
        # Calculate Final Score
    def create_performance_summary(self, story, styles):
        story.append(PageBreak())
        section_title_style = ParagraphStyle(
            'SectionTitle',
            parent=styles['Heading2'],
            fontSize=16,
            spaceBefore=20,
            spaceAfter=12,
            textColor=colors.HexColor('#2E4053')
        )
        
        story.append(Paragraph("Performance Summary", section_title_style))

        # Add descriptive text
        summary_intro = """The following summary presents a detailed breakdown of your reflex performance across both sides. 
        The assessment evaluates multiple aspects including reaction time, accuracy, and consistency for both left and right sides."""

        story.append(Paragraph(summary_intro, styles['Normal']))
        story.append(Spacer(1, 20))


        # Helper function to get level data based on score
        def get_assessment_level(score):
            if score >= 8.5:
                return {
                    'level': 'EXCELLENT',
                    'color': '#27AE60',
                    'percentage': score * 10  # Convert to percentage
                }
            elif score >= 7:
                return {
                    'level': 'GOOD',
                    'color': '#F39C12',
                    'percentage': score * 10
                }
            elif score >= 5:
                return {
                    'level': 'FAIR',
                    'color': '#E67E22',
                    'percentage': score * 10
                }
            else:
                return {
                    'level': 'Devloping',
                    'color': '#E74C3C',
                    'percentage': score * 10
                }

        # Helper function to create level indicator bar

        # Get level data based on final score
        level_data = get_assessment_level(self.final_score)
        
        # Create assessment box with score
        assessment_content = [
            [Paragraph(f"""
            <font color='{level_data['color']}' size='11'><b>{level_data['level']}</b></font>
            <br/>
            <font color="#7F8C8D" size='8'><b>Overall Score: {self.final_score:.1f}/10</b></font>
            <br/>
            <font color='#5D6D7E' size='9'>Assessment based on overall performance metrics</font>
            """, styles['Normal'])]
        ]
        
        assessment_box = Table(assessment_content, colWidths=[6*inch])
        assessment_box.setStyle(TableStyle([
            ('BOX', (0, 0), (-1, -1), 2, colors.HexColor('#2E4053')),
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F4F6F7')),
            ('PADDING', (0, 0), (-1, -1), 15),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ]))
        story.append(assessment_box)
        story.append(Spacer(1, 20))

        # Rest of the performance summary table
        summary_data = [
            ["Metrics", "Right Side", "Left Side"],
            ["Successful Reactions", self.right_side_count, self.left_side_count],
            ["Average Reaction Time", f'{int(self.avg_right_reaction_time)} ms', f'{int(self.avg_left_reaction_time)} ms'],
            ["Fastest Reaction", f'{self.right_fastest_reaction} ms', f'{self.left_fastest_reaction} ms'],
            ["Slowest Reaction", f'{self.right_slowest_reaction} ms', f'{self.left_slowest_reaction} ms'],
            ["Missed Targets", 10-self.right_side_count, 10-self.left_side_count]
        ]
        
        summary_table = Table(summary_data, colWidths=[2.5*inch, 2.5*inch, 2.5*inch])
        summary_table.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2E4053')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('PADDING', (0, 0), (-1, -1), 8),
        ]))
        
        story.append(summary_table)
        story.append(Spacer(1, 30))
        
        return story

    def create_detailed_metrics(self, story, styles):
        section_title_style = ParagraphStyle(
            'SectionTitle',
            parent=styles['Heading2'],
            fontSize=16,
            spaceBefore=20,
            spaceAfter=12,
            textColor=colors.HexColor('#2E4053')
        )
        
        story.append(Paragraph("Detailed Performance Metrics", section_title_style))
        
        # Create detailed metrics table
        metrics_data = [
            ["Performance Metric", "Left Side", "Right Side", "Overall"],
            ["Reaction Time Score (RTS)", f"{self.left_rts:.1f}", f"{self.right_rts:.1f}", f"{self.overall_rts:.1f}"],
            ["Accuracy Score (AS)", f"{self.left_as:.1f}%", f"{self.right_as:.1f}%", f"{self.overall_as:.1f}%"],
            ["Consistency Score (CS)", f"{self.left_cs:.1f}", f"{self.right_cs:.1f}", f"{self.overall_cs:.1f}"],
        ]
        
        metrics_table = Table(metrics_data, colWidths=[2.5*inch, 1.5*inch, 1.5*inch, 1.5*inch])
        metrics_table.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2E4053')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('PADDING', (0, 0), (-1, -1), 8),
        ]))
        
        story.append(metrics_table)
        story.append(Spacer(1, 20))
        
        # Additional metrics
        additional_metrics = [
            ["Overall Metrics", "Value", "Interpretation"],
            ["Lateral Balance Score (LBS)", f"{self.lbs:.1f}", "Measures balance between both side performance"],
            ["Missed Tap Penalty (MTP)", f"{self.mtp:.1f}", "Penalty points for missed targets"],
            ["Final Overall Score", f"{self.final_score:.1f}/10", "overall performance evaluation"]
        ]
        
        additional_table = Table(additional_metrics, colWidths=[2.3*inch, 1.4*inch, 3.3*inch])
        additional_table.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2E4053')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (1, 0), (1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('PADDING', (0, 0), (-1, -1), 8),
        ]))
        
        story.append(additional_table)
        
        # Add performance analysis text
        story.append(Spacer(1, 20))
        note_style = ParagraphStyle(
        'Note',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#666666'),
        leftIndent=20,
        rightIndent=20,
        spaceBefore=20
        )
    
        analysis_text = f"""
        
        <b>Quick Interpretetion:</b>
        
        The athlete demonstrated {'balanced' if abs(self.left_rts - self.right_rts) < 10 else 'unbalanced'} performance between left and right sides. 
        The overall reaction time score of {self.overall_rts:.1f} indicates {'excellent' if self.overall_rts > 90 else 'good' if self.overall_rts > 80 else 'fair'} performance relative to the optimal reaction time({self.optimal_reaction_time} ms).
        
        Accuracy was {'consistent' if abs(self.left_as - self.right_as) < 10 else 'inconsistent'} across both sides, with an overall accuracy score of {self.overall_as:.1f}%. 
        The consistency score shows that the athlete maintained {'stable' if self.overall_cs > 85 else 'variable'} performance throughout the drill.
        
        The final score of {self.final_score:.1f} suggests {'excellent' if self.final_score > 90 else 'good' if self.final_score > 80 else 'fair'} overall performance.
        """
        
        story.append(Paragraph(analysis_text, note_style))
        
        return story

    def create_score_understanding(self, story, styles):
        # Add page break before new sectio

        story.append(PageBreak())
        # Custom styles for this section
        section_title_style = ParagraphStyle(
            'SectionTitle',
            parent=styles['Heading2'],
            fontSize=20,
            spaceBefore=20,
            spaceAfter=12,
            textColor=colors.HexColor('#2E4053')
        )
        
        subsection_style = ParagraphStyle(
            'SubSection',
            parent=styles['Heading3'],
            fontSize=14,
            spaceBefore=15,
            spaceAfter=8,
            textColor=colors.HexColor('#2E4053')
        )
        
        metric_title_style = ParagraphStyle(
            'MetricTitle',
            parent=styles['Heading4'],
            fontSize=12,
            spaceBefore=12,
            spaceAfter=6,
            textColor=colors.HexColor('#34495E')
        )
        
        body_text_style = ParagraphStyle(
            'BodyText',
            parent=styles['Normal'],
            fontSize=10,
            leading=14,
            spaceBefore=6,
            spaceAfter=8
        )
        
        # Main title
        story.append(Paragraph("Understanding Your Scores", section_title_style))
        
        intro_text = """This section provides a detailed explanation of each performance metric in your assessment. 
        Understanding these scores will help you identify your strengths and areas for improvement. Each metric is 
        explained with its calculation method, interpretation, and your specific performance."""
        story.append(Paragraph(intro_text, body_text_style))
        story.append(Spacer(1, 15))

        # 1. Reaction Time Score (RTS)
        story.append(Paragraph("1. Reaction Time Score (RTS)", subsection_style))
        
        rts_data = [
            ["Component", "Your Score", "Optimal Range"],
            ["Left Side", f"{self.left_rts:.1f}", "90-100"],
            ["Right Side", f"{self.right_rts:.1f}", "90-100"],
            ["Overall", f"{self.overall_rts:.1f}", "90-100"]
        ]
        
        rts_table = Table(rts_data, colWidths=[2*inch, 1.5*inch, 1.5*inch])
        rts_table.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495E')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('PADDING', (0, 0), (-1, -1), 8),
        ]))
        
        story.append(rts_table)
        story.append(Spacer(1, 10))
        
        rts_explanation = f"""
        <b>What it measures:</b> The Reaction Time Score evaluates how quickly you respond to visual stimuli compared 
        to an optimal reaction time of 500ms.<br/><br/>
        
        <b>Calculation:</b> RTS = 100 × (500ms/Your Average Reaction Time)<br/><br/>
        
        <b>Your Performance:</b> Your overall RTS of {self.overall_rts:.1f} indicates 
        {'<font color="#27AE60">Outstanding reflexes</font>' if self.overall_rts > 90 else '<font color="#F39C12">Good reflexes</font>' if self.overall_rts > 80 else '<font color="#E74C3C">Room for improvement</font>'}.
        {'Your left side ('+f"{self.left_rts:.1f}"+') and right side ('+f"{self.right_rts:.1f}"+') scores show ' + 
        ('balanced performance.' if abs(self.left_rts - self.right_rts) < 10 else 'some asymmetry that could be addressed through training.')}
        """
        story.append(Paragraph(rts_explanation, body_text_style))
        story.append(Spacer(1, 15))
        
        # 2. Accuracy Score (AS)
        story.append(Paragraph("2. Accuracy Score (AS)", subsection_style))
        
        as_data = [
            ["Component", "Your Score", "Optimal Range"],
            ["Left Side", f"{self.left_as:.1f}%", "90-100%"],
            ["Right Side", f"{self.right_as:.1f}%", "90-100%"],
            ["Overall", f"{self.overall_as:.1f}%", "90-100%"]
        ]
        
        as_table = Table(as_data, colWidths=[2*inch, 1.5*inch, 1.5*inch])
        as_table.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495E')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('PADDING', (0, 0), (-1, -1), 8),
        ]))
        
        story.append(as_table)
        story.append(Spacer(1, 10))
        
        as_explanation = f"""
        <b>What it measures:</b> The Accuracy Score represents your success rate in hitting targets within the allowed time window.
        <br/><br/>
        <b>Calculation:</b> AS = 100 × (Number of Successful Taps ÷ Total Targets)
        <br/><br/>
        <b>Your Performance:</b> Your overall accuracy of {self.overall_as:.1f}% shows 
        {'<font color="#27AE60">excellent precision</font>' if self.overall_as > 90 else '<font color="#F29C12">good accuracy</font>' if self.overall_as > 80 else '<font color="#E74C3C">room for improvement</font>'}.
        You missed {self.missed_targets} targets out of 20, {'which is within acceptable range.' if self.missed_targets <= 2 
        else 'suggesting focus on accuracy might be beneficial.'}
        """
        story.append(Paragraph(as_explanation, body_text_style))
        story.append(Spacer(1, 15))
        
        # 3. Consistency Score (CS)
        story.append(PageBreak())
        story.append(Paragraph("3. Consistency Score (CS)", subsection_style))
        
        cs_data = [
            ["Component", "Your Score", "Optimal Range"],
            ["Left Side", f"{self.left_cs:.1f}", "85-100"],
            ["Right Side", f"{self.right_cs:.1f}", "85-100"],
            ["Overall", f"{self.overall_cs:.1f}", "85-100"]
        ]
        
        cs_table = Table(cs_data, colWidths=[2*inch, 1.5*inch, 1.5*inch])
        cs_table.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495E')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('PADDING', (0, 0), (-1, -1), 8),
        ]))
        
        story.append(cs_table)
        story.append(Spacer(1, 10))
        
        cs_explanation = f"""
        <b>What it measures:</b> The Consistency Score evaluates how stable your reaction times are throughout the test.
        <br/><br/>
        <b>Calculation:</b> CS = 100 × (1 - Standard Deviation of Reaction Times ÷ Average Reaction Time)
        <br/><br/>
        <b>Your Performance:</b> Your overall consistency score of {self.overall_cs:.1f} indicates 
        {'<font color="#27AE60">very stable performance</font>' if self.overall_cs > 90 else '<font color="#F29C12">reasonably stable performance</font>' if self.overall_cs > 80 
        else '<font color="#E74C3C">variable performance that could be improved with practice</font>'}. 
        {'Both sides show similar consistency.' if abs(self.left_cs - self.right_cs) < 5 
        else 'There is some variation between left and right side consistency that could be addressed.'}
        """
        story.append(Paragraph(cs_explanation, body_text_style))
        story.append(Spacer(1, 15))
        
        # 4. Lateral Balance Score (LBS)
        story.append(Paragraph("4. Lateral Balance Score (LBS)", subsection_style))
        
        lbs_box_style = TableStyle([
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495E')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('PADDING', (0, 0), (-1, -1), 8),
        ])
        
        lbs_data = [["Your LBS Score", "Optimal Range"], [f"{self.lbs:.1f}", "90-100"]]
        lbs_table = Table(lbs_data, colWidths=[2.5*inch, 2.5*inch])
        lbs_table.setStyle(lbs_box_style)
        
        story.append(lbs_table)
        story.append(Spacer(1, 10))
        
        lbs_explanation = f"""
        <b>What it measures:</b> The Lateral Balance Score assesses the symmetry between your left and right side performance.
        <br/><br/>
        <b>Calculation:</b> LBS = 100 - |Left Side Average - Right Side Average| ÷ Overall Average × 100
        <br/><br/>
        <b>Your Performance:</b> Your LBS of {self.lbs:.1f} shows 
        {'<font color="#27AE60">excellent balance between sides</font>' if self.lbs > 90 else '<font color="#F29C12">ood balance between sides</font>' if self.lbs > 80 
        else '<font color="#E74C3C">notable difference between left and right side performance</font>'}. 
        {'This indicates well-developed bilateral coordination.' if self.lbs > 90 
        else 'Some targeted training might help improve bilateral balance.'}
        """

        story.append(Paragraph(lbs_explanation, body_text_style))
        story.append(Spacer(1, 10))
        # story.append(PageBreak())
        

    # Update the Final Score section
        story.append(Paragraph("5. Final Overall Score", subsection_style))
        
        # Update the performance levels based on 10-point scale
        performance_level = (
            'Excellent' if self.final_score >= 8.5 
            else 'Good' if self.final_score >= 7 
            else 'Fair' if self.final_score >= 5 
            else 'Devloping'
        )
        
        final_data = [
            ["Your Final Score", "Performance Level", "optimal Range"],
            [f"{self.final_score:.2f}/10", performance_level,7.5-10]
        ]
        
        final_table = Table(final_data, colWidths=[2*inch, 2*inch, 2*inch])
        final_table.setStyle(lbs_box_style)
        
        story.append(final_table)
        story.append(Spacer(1, 5))
        
        final_explanation = f"""
        <b>What it represents:</b> The Final Score is calculated based on your reaction speed for each target, with points awarded as follows:
        <br/><br/>
        • 0.5 points: Reactions under 300ms (optimal response)
        <br/>
        • 0.3-0.5 points: Reactions between 300-500ms (sliding scale)
        <br/>
        • 0.3 points: Reactions over 500ms
        <br/>
        • 0 points: Missed targets or invalid responses
        <br/><br/>
        <b>Calculation Method:</b>
        • Each successful reaction earns points based on reaction time
        • Points are summed across all attempts
        • Maximum possible score is 10 points
        <br/><br/>
        <b>Your Performance:</b> Your final score of {self.final_score:.2f}/10 indicates 
        {'<font color="#27AE60">excellent reflexes and consistent performance</font>' if self.final_score >= 8.5 
        else '<font color="#F29C12">good overall performance with room for optimization</font>' if self.final_score >= 7 
        else '<font color="#E67E22">fair performance that can be improved with practice</font>' if self.final_score >= 5
        else '<font color="#E74C3C">a need for focused practice to improve reaction speed and accuracy</font>'}.
        
        You achieved this score by {'consistently hitting targets with optimal timing' if self.final_score >= 8.5
        else 'maintaining good response times across most attempts' if self.final_score >= 7
        else 'successfully hitting targets but with varied response times' if self.final_score >= 5
        else 'showing potential but needing more practice for consistency'}.
        """
        
        story.append(Paragraph(final_explanation, body_text_style))
            
        return story


    # Determine which recommendation to use based on metric value
    def create_recommendation_box(self,title, metric_value, ranges, recommendations,story,styles):
        recommendation_text = ""
        metric_level = ""
        box_color = ""
        
        if title == "Reaction Time":
            if metric_value >= 90:
                recommendation_text = recommendations[0]
                metric_level = "Excellent"
                box_color = "#27AE60"
            elif 90 > metric_value >= 80:
                recommendation_text = recommendations[1]
                metric_level = "Good"
                box_color = "#F39C12"
            elif 80 > metric_value >= 70:
                recommendation_text = recommendations[2]
                metric_level = "Moderate"
                box_color = "#E67E22"
            else:
                recommendation_text = recommendations[3]
                metric_level = "Devloping"
                box_color = "#E74C3C"
        
        elif title == "Accuracy":
            if metric_value >= 90:
                recommendation_text = recommendations[0]
                metric_level = "Excellent"
                box_color = "#27AE60"
            elif 90 > metric_value >= 80:
                recommendation_text = recommendations[1]
                metric_level = "Good"
                box_color = "#F39C12"
            else:
                recommendation_text = recommendations[2]
                metric_level = "Devloping"
                box_color = "#E74C3C"
        
        elif title == "Consistency":
            if metric_value >= 85:
                recommendation_text = recommendations[0]
                metric_level = "Excellent"
                box_color = "#27AE60"
            elif 85 > metric_value >= 75:
                recommendation_text = recommendations[1]
                metric_level = "Good"
                box_color = "#F39C12"
            else:
                recommendation_text = recommendations[2]
                metric_level = "Devloping"
                box_color = "#E74C3C"

        elif title == "Lateral Balance":
            if metric_value >= 90:
                recommendation_text = recommendations[0]
                metric_level = "Excellent"
                box_color = "#27AE60"
            elif 90 > metric_value >= 80:
                recommendation_text = recommendations[1]
                metric_level = "Good"
                box_color = "#F39C12"
            else:
                recommendation_text = recommendations[2]
                metric_level = "Devloping"
                box_color = "#E74C3C"
        
        # Create recommendation box
        box_data = [
            [Table(
                [[Paragraph(f"{title} Recommendations", styles['Heading3'])]],
                colWidths=[6*inch],
                style=TableStyle([
                    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor(box_color)),
                    ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('PADDING', (0, 0), (-1, -1), 8),
                ])
            )],
            [Table(
                [[
                    Paragraph(f"Current Level: {metric_level}", styles['Normal']),
                    Paragraph(f"Score: {metric_value:.2f}", styles['Normal'])
                ]],
                colWidths=[3*inch, 3*inch],
                style=TableStyle([
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F8F9F9')),
                    ('PADDING', (0, 0), (-1, -1), 8),
                ])
            )],
            [Paragraph(recommendation_text, styles['Normal'])]
        ]
        
        main_box = Table(
            box_data,
            colWidths=[6*inch],
            style=TableStyle([
                ('BOX', (0, 0), (-1, -1), 1, colors.grey),
                ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#FFFFFF')),
                ('PADDING', (0, 0), (-1, -1), 10),
            ])
        )
        
        story.append(main_box)
        story.append(Spacer(1, 20))

    def generate_recommendations(self,story,styles):

        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=20,
            spaceAfter=20,
            textColor=colors.HexColor('#2E4053')
        )
        
        story.append(PageBreak())
        story.append(Paragraph("Personalized Recommendations", title_style))
        
        # Introduction paragraph
        intro_style = ParagraphStyle(
            'Intro',
            parent=styles['Normal'],
            fontSize=12,
            leading=14,
            spaceBefore=10,
            spaceAfter=20
        )
        
        story.append(Paragraph(
            "Based on your performance metrics, we've prepared personalized recommendations to help you improve your reflex speed and motor responses. "
            "Focus on these exercises and gradually increase difficulty as you progress.",
            intro_style
        ))

        reaction_recommendations = [
            "Outstanding reflexes! To maintain this level, try advanced reaction drills like multiple choice reaction games, sports-specific reaction drills, or using reaction training apps. Include compound movements like jump-to-catch exercises to challenge your whole-body reactions.",
            "Good reaction speed! Focus on improving with exercises like ball drops, light-based reaction games, and agility ladder drills with directional changes. Adding cognitive challenges during reactions (like color-matching) can help boost performance.",
            "Your reactions show promise. Practice basic drills like simple ball catches, partner-assisted reaction games, and basic agility ladder exercises. Focus on maintaining attention and reducing anticipation during drills.",
            "Start with fundamental reaction training. Use simple visual cues with longer response windows, practice basic hand-eye coordination exercises, and work on maintaining focus during short drill sessions. Gradually decrease response time as you improve."
        ]
        self.create_recommendation_box("Reaction Time", self.overall_rts, [], reaction_recommendations,story,styles)

        # Accuracy Recommendations
        accuracy_recommendations = [
            "Excellent precision! Challenge yourself further with smaller targets, moving targets, or multiple target sequences. Try advanced drills that combine accuracy with speed changes or direction changes to maintain your high performance level.",
            "Good accuracy demonstrated. To improve, practice with varied target sizes and distances. Include exercises that require precise movements under time pressure, and work on maintaining accuracy during longer sessions.",
            "Focus on building accuracy through target practice starting with larger, stationary targets. Practice deliberate, controlled movements before adding speed. Use visual tracking exercises and gradually progress to smaller or moving targets."
        ]
        self.create_recommendation_box("Accuracy", self.overall_as, [], accuracy_recommendations,story,styles)

        # Consistency Recommendations
        consistency_recommendations = [
            "Your performance is highly consistent. To maintain this level, try advanced variability training like changing speeds, directions, or adding secondary tasks while maintaining consistent response times.",
            "Good consistency shown. Work on rhythm-based exercises and tempo training to improve stability. Practice maintaining consistent performance under various conditions like different speeds or positions.",
            "Build consistency through structured practice sessions. Start with fixed-pace exercises, use metronome-guided drills, and focus on maintaining steady rhythm before increasing speed or complexity."
        ]
        self.create_recommendation_box("Consistency", self.overall_cs, [], consistency_recommendations,story,styles)

        # Lateral Balance Recommendations
        lateral_recommendations = [
            "Excellent bilateral performance! Continue challenging both sides equally with advanced bilateral drills, alternating hand exercises, and complex movement patterns that require coordinated responses.",
            "Good bilateral balance. Focus on the slightly weaker side with targeted practice. Include exercises that force equal use of both sides, and practice alternating hand responses to even out performance.",
            "Work on improving bilateral coordination through basic alternating exercises. Start with simple bilateral movements, practice equal repetitions on both sides, and gradually increase complexity as balance improves."
        ]
        self.create_recommendation_box("Lateral Balance", self.lbs, [], lateral_recommendations,story,styles)

        # Final note
        note_style = ParagraphStyle(
            'Note',
            parent=styles['Normal'],
            fontSize=9,
            textColor=colors.HexColor('#666666'),
            leftIndent=20,
            rightIndent=20,
            spaceBefore=20
        )

        story.append(Paragraph(
            "<i>Note: These recommendations are based on your current performance metrics. Start with easier variations "
            "and progress gradually. Regular practice is key to improving reaction time and accuracy. If you experience "
            "any discomfort during exercises, please consult with your healthcare provider.</i>",
            note_style
        ))
    
    # Title styling
    def create_reflex_training_plan(self,story, styles, total_score):
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=1,
            textColor=colors.HexColor('#2E4053')
        )

        story.append(Paragraph("Personalized Reflex Development Plan", title_style))
        story.append(Spacer(1, 5))
        
        # Create tables for each phase of training
        def create_phase_table(phase_title, exercises, duration, frequency):
            data = [
                [Paragraph(f"<b>{phase_title}</b>", styles['Normal']), 
                Paragraph(f"<b>Duration:</b> {duration}", styles['Normal']),
                Paragraph(f"<b>Frequency:</b> {frequency}", styles['Normal'])],
                [Paragraph("<b>Exercise</b>", styles['Normal']),
                Paragraph("<b>Sets × Reps</b>", styles['Normal']),
                Paragraph("<b>Progression</b>", styles['Normal'])]
            ]
            
            for exercise in exercises:
                data.append([
                    Paragraph(exercise[0], styles['Normal']),
                    Paragraph(exercise[1], styles['Normal']),
                    Paragraph(exercise[2], styles['Normal'])
                ])
            
            table = Table(data, colWidths=[3*inch, 1.5*inch, 2*inch])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#EBF5FB')),
                ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#2E4053')),
                ('TEXTCOLOR', (0, 1), (-1, 1), colors.white),
                ('GRID', (0, 0), (-1, -1), 1, colors.grey),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('PADDING', (0, 0), (-1, -1), 8),
                ('FONTNAME', (0, 0), (-1, 1), 'Helvetica-Bold'),
            ]))
            return table

        # Define exercise programs based on performance
        if total_score < 70:
            # Basic Reflex Program
            phase1_exercises = [
                ("Light Ball Reaction Catch", "3 × 30s each", "Decrease distance"),
                ("Single-Hand Target Tap", "3 × 20 each", "Reduce response window"),
                ("Basic Directional Response", "3 × 10 each side", "Add movement patterns")
            ]
            
            phase2_exercises = [
                ("Alternating Hand Taps", "3 × 45s", "Increase speed"),
                ("Response Pattern Drill", "3 × 12 each side", "Add complexity"),
                ("Reflex Light Training", "3 × 16 patterns", "Decrease time window")
            ]
            
            phase3_exercises = [
                ("Multi-Target Response", "3 × 10 each", "Add distractions"),
                ("Reaction Ball Drills", "3 × 15", "Increase bounce variations"),
                ("Dynamic Response Pattern", "3 × 30s", "Add cognitive load")
            ]
        
        elif total_score < 85:
            # Intermediate Reflex Program
            phase1_exercises = [
                ("Dual Hand Response Drill", "4 × 45s", "Add pattern complexity"),
                ("Moving Target Response", "4 × 30s each", "Increase movement speed"),
                ("Peripheral Vision Reaction", "3 × 12 each", "Expand visual field")
            ]
            
            phase2_exercises = [
                ("Multi-Directional Response", "3 × 60s", "Add secondary tasks"),
                ("Reactive Pattern Matrix", "4 × 15 each", "Decrease rest time"),
                ("Speed Response Circuit", "3 × 45s", "Add decision making")
            ]
            
            phase3_exercises = [
                ("Choice Reaction Training", "3 × 10 each", "Add multiple stimuli"),
                ("Complex Pattern Response", "3 × 12", "Increase pattern speed"),
                ("Agility Reaction Drill", "3 × 8 each side", "Add movement complexity")
            ]
        
        else:
            # Advanced Reflex Program
            phase1_exercises = [
                ("Elite Response Pattern", "4 × 12 each", "Add cognitive challenge"),
                ("Multi-Stimulus Response", "3 × 45s", "Increase stimulus variety"),
                ("Advanced Reaction Circuit", "3 × 10 each", "Reduce recovery time")
            ]
            
            phase2_exercises = [
                ("Complex Decision Response", "4 × 30s each", "Add decision complexity"),
                ("High-Speed Pattern Matrix", "3 × 16 total", "Increase pattern speed"),
                ("Elite Agility Response", "3 × 4 each way", "Add movement variations")
            ]
            
            phase3_exercises = [
                ("Competition Speed Drill", "3 × 45s", "Add competitive element"),
                ("Advanced Response Flow", "3 × 60s", "Minimize transition time"),
                ("Elite Integration Complex", "3 × 30s each", "Add sport-specific elements")
            ]

        # Add tables to story
        story.append(create_phase_table("Phase 1: Foundation (Weeks 1-2)", 
                                    phase1_exercises, 
                                    "2 Weeks", 
                                    "3-4 sessions/week"))
        story.append(Spacer(1, 15))
        
        story.append(create_phase_table("Phase 2: Development (Weeks 3-4)", 
                                    phase2_exercises, 
                                    "2 Weeks", 
                                    "3-4 sessions/week"))
        story.append(Spacer(1, 15))
        
        story.append(create_phase_table("Phase 3: Advanced Integration (Weeks 5-6)", 
                                    phase3_exercises, 
                                    "2 Weeks", 
                                    "3-4 sessions/week"))
        
        # Important Notes Section
        story.append(Spacer(1, 20))
        notes_style = ParagraphStyle(
            'Notes',
            parent=styles['Normal'],
            fontSize=10,
            textColor=colors.HexColor('#2E4053'),
            borderColor=colors.HexColor('#2E4053'),
            borderWidth=1,
            borderPadding=10,
            borderRadius=5
        )
        
        important_notes = """
        <b>Important Notes:</b>
        • Begin each session with proper visual and neural warm-up exercises
        • Focus on quick, precise movements rather than just speed
        • Maintain proper form throughout all drills - accuracy before speed
        • Take regular breaks to prevent neural fatigue
        • Stay well-hydrated and ensure proper rest between sessions
        • If experiencing eye strain or unusual fatigue, stop and consult your instructor
        • Schedule a follow-up assessment after completing the 6-week program
        • Progress through variations only when maintaining high accuracy (>90%)
        """
        
        story.append(Paragraph(important_notes, notes_style))
        
        return story
    
    def create_conclusion(self, story, styles):
        # Add page break before conclusion
        story.append(PageBreak())
        title_style = ParagraphStyle(
            'ConclusionTitle',
            parent=styles['Heading1'],
            fontSize=20,
            spaceAfter=20,
            textColor=colors.HexColor('#2E4053')
        )
        
        subtitle_style = ParagraphStyle(
            'ConclusionSubtitle',
            parent=styles['Heading2'],
            fontSize=14,
            spaceBefore=15,
            spaceAfter=10,
            textColor=colors.HexColor('#2E4053')
        )
        
        content_style = ParagraphStyle(
            'ConclusionContent',
            parent=styles['Normal'],
            fontSize=11,
            leading=14,
            spaceBefore=5,
            spaceAfter=10,
            alignment=4
        )
        
        # Add main title
        story.append(Paragraph("Assessment Conclusion", title_style))
        # Overall Assessment
        
        # Determine performance level and specific observations
        performance_level = ('excellent' if self.final_score > 90 
                            else 'good' if self.final_score > 80 
                            else 'fair' if self.final_score > 70 
                            else 'Devloping')
        
        lateral_balance = ('well-balanced' if self.lbs > 85 
                        else 'moderately balanced' if self.lbs > 75 
                        else 'shows notable asymmetry')
        
        consistency_level = ('highly consistent' if self.overall_cs > 85 
                            else 'moderately consistent' if self.overall_cs > 75 
                            else 'shows variable performance')
        
        # Generate overall assessment text
        assessment_text = f"""
        The athlete has demonstrated <b>{performance_level}</b> performance in the reflex drill assessment, 
        achieving an overall score of {self.final_score:.1f}. Their performance was characterized by {lateral_balance} 
        lateral coordination (LBS: {self.lbs:.1f}) and {consistency_level} execution throughout the drill 
        (CS: {self.overall_cs:.1f}).
        
        The average reaction time of {self.avg_reaction_time:.1f}ms indicates 
        {'exceptional' if self.overall_rts > 90 else 'good' if self.overall_rts > 80 else 'moderate'} neural response, 
        while the accuracy rate of {self.overall_as:.1f}% shows 
        {'excellent' if self.overall_as > 90 else 'good' if self.overall_as > 80 else 'fair'} target acquisition capabilities.
        """
        
        story.append(Paragraph(assessment_text, content_style))
        story.append(Spacer(1, 15))
        
        # Next Steps and Recommendations with enhanced visual presentation
        story = self.create_reflex_training_plan(story,styles,self.final_score)
        return story
    
    def create_final_branding_page(self,story, styles):
        from reportlab.lib import colors
        from reportlab.lib.units import inch
        from reportlab.platypus import Spacer, Table, TableStyle, Image
        from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

        story.append(PageBreak())
        story.append(Spacer(1, 2*inch))
        
        # Large centered logo
        logo_table = Table([[Image('hyperlab_logo.png', width=3*inch, height=1.2*inch)]], 
                        colWidths=[7.5*inch])
        logo_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ]))
        story.append(logo_table)
        
        story.append(Spacer(1, inch))
        
        # Company information
        info_style = ParagraphStyle(
            'CompanyInfo',
            parent=styles['Normal'],
            fontSize=12,
            alignment=TA_CENTER,
            textColor=colors.HexColor('#2E4053'),
            spaceAfter=12
        )
        
        contact_style = ParagraphStyle(
            'ContactInfo',
            parent=styles['Normal'],
            fontSize=10,
            alignment=TA_CENTER,
            textColor=colors.HexColor('#5D6D7E'),
            spaceAfter=8
        )
        
        info_data = [
            [Paragraph("<b>HyperLab Sportech Pvt. Ltd.</b>", info_style)],
            [Paragraph("Advanced Performance Assessment & Training Solutions", contact_style)],
            [Paragraph("https://www.hyperlab.life/ | contact@hyperlab.life", contact_style)],
            [Paragraph("support@hyperlab.life", contact_style)],
        ]
        
        info_table = Table(info_data, colWidths=[7.5*inch])
        info_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ]))
        story.append(info_table)
        
        story.append(Spacer(1, 2*inch))
        
        # Bottom decorative element
        footer_text = "Excellence in Sports Science & Technology"
        footer_style = ParagraphStyle(
            'BrandingFooter',
            parent=styles['Normal'],
            fontSize=14,
            alignment=TA_CENTER,
            textColor=colors.HexColor('#2E4053')
        )
        
        story.append(Paragraph(footer_text, footer_style))
        
        # Add decorative line
        line_table = Table([['']], colWidths=[5*inch], rowHeights=[1])
        line_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#2E4053')),
            ('LINEBELOW', (0, 0), (-1, -1), 2, colors.HexColor('#2E4053'))
        ]))
        story.append(line_table)
        
        return story
    def create_reflex_report(self,student_name, instructor_name, scores):
        # Create the PDF document
        doc = SimpleDocTemplate(
            f"reflex_report_{student_name.replace(' ', '_')}.pdf",
            pagesize=A4,
            rightMargin=0.5*inch,
            leftMargin=0.5*inch,
            topMargin=0.5*inch,
            bottomMargin=0.5*inch
        )
        
        # Container for the 'Flowables'
        story = []
        styles = getSampleStyleSheet()
        
        # Create first page
        story = self.create_first_page(story, styles)
        
        # Calculate metrics
        self.calculate_metrics(scores)
        
        # Add performance summary
        story = self.create_performance_summary(story, styles)

        story = self.create_detailed_metrics(story, styles)
        
        story = self.create_score_understanding(story, styles)
        # Add page break before detailed metrics

        self.generate_recommendations(story, styles)
        
        story = self.create_conclusion(story, styles)
        story=self.create_final_branding_page(story,styles)
        # Build the PDF
        doc.build(story)
    # Example usag



if __name__ == "__main__":
    student_name = "devang babel"
    instructor_name = "Dr. aditya"
    scores = [765, -765, 555, -300, 400, -500, 600, 0, -500, -600, -800, -900, -700, -900, 700, 600, 500, 499, 0, 399]
    rep=reflex_report()
    rep.create_reflex_report(student_name, instructor_name, scores)
    import os
    os.startfile('reflex_report_devang_babel.pdf')